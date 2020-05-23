from django import forms
# from BugTracker.models import BugTicket


class TicketAdd(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
