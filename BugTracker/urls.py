"""BugTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BugTracker import views
from django.conf import settings
from BugTracker.models import BugTicket
from django.conf.urls.static import static

admin.site.register(BugTicket)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('addticket/', views.add_ticket, name='add_ticket'),
    path('editticket/<int:id>/', views.edit_ticket, name='edit_ticket'),
    path('tickets/<int:id>/', views.view_ticket, name='ticket_view'),
    path('login/', views.loginview, name='login_view'),
    path('logout/', views.logoutview, name='logout_view'),
    path('changeticket/<int:id>/', views.affect_ticket, name='affect_new'),
    path('userpage/<int:id>/', views.userpage, name='user_page')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
