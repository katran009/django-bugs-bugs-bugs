from django.shortcuts import render, HttpResponseRedirect, reverse
from BugTracker.models import BugTicket
from BugTracker.forms import TicketAdd, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def index(request):
    html = 'index.html'
    data = BugTicket.objects.all().order_by('post_time')
    new = BugTicket.objects.filter(ticket_status='N').order_by('post_time')
    in_progress = BugTicket.objects.filter(
        ticket_status='IP').order_by('-post_time')
    done = BugTicket.objects.filter(ticket_status='D').order_by('post_time')
    invalid = BugTicket.objects.filter(
        ticket_status='IV').order_by('post_time')
    return render(request, html, {
        'data': data,
        'new': new,
        'in_progress': in_progress,
        'done': done,
        'invalid': invalid
    }
    )


@login_required
def view_ticket(request, id):
    html = 'tickets.html'
    data = BugTicket.objects.filter(id=id)
    return render(request, html, {'data': data})


@login_required
def add_ticket(request):
    html = 'add_form.html'
    if request.method == 'POST':
        form = TicketAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BugTicket.objects.create(
                ticket_author=request.user,
                title=data['title'],
                description=data['description'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = TicketAdd()
    return render(request, html, {'form': form})


@login_required
def edit_ticket(request, id):
    html = 'editticket.html'
    instance = BugTicket.objects.get(id=id)
    if request.method == 'POST':
        form = TicketAdd(request.POST, initial={
            'title': instance.title,
            'description': instance.description
        })
        if form.is_valid():

            instance.title = form.cleaned_data['title']
            instance.description = form.cleaned_data['description']
            instance.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = TicketAdd(initial={
        'title': instance.title,
        'description': instance.description
    })
    return render(request, html, {'form': form})


@login_required
def affect_ticket(request, id):
    instance = BugTicket.objects.get(id=id)
    if request.method == 'POST':
        action = request.POST.get('action')
        print(action)
        if action == '2':
            instance.ticket_status = 'IP'
            instance.assigned_user = request.user
            instance.finished_user = None
            instance.save()
            return HttpResponseRedirect(reverse('ticket_view', args=[id]))
        if action == '3':
            instance.ticket_status = 'D'
            instance.assigned_user = None
            instance.finished_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('ticket_view', args=[id]))
        if action == '4':
            instance.ticket_status = 'IV'
            instance.assigned_user = None
            instance.finished_user = None
            instance.save()
            return HttpResponseRedirect(reverse('ticket_view', args=[id]))
        if action == '1':
            instance.ticket_status = 'N'
            instance.assigned_user = None
            instance.finished_user = None
            instance.save()
            return HttpResponseRedirect(reverse('ticket_view', args=[id]))


def loginview(request):
    html = 'add_form.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def userpage(request, id):
    html = 'user.html'
    user = User.objects.get(pk=id)
    created = BugTicket.objects.filter(ticket_author_id=id)
    assigned = BugTicket.objects.filter(assigned_user_id=id)
    finished = BugTicket.objects.filter(finished_user_id=id)
    return render(request, html, {
        'created': created,
        'finished': finished,
        'assigned': assigned,
        'user': user
    })
