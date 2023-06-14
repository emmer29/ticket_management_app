"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('', include('dashboard.urls')),
#  path('ticket/', include('ticket.urls')),
#    path('accounts/', include('users.urls', namespace='users'))
#]

from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from dashboard import views as dashboard_views
from ticket import views as ticket_views

urlpatterns = [
    path('', user_views.login_user, name='home'),
    path('login/', user_views.login_user, name='login'),
    path('register-customer/', user_views.register_customer, name='register-customer'),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('ticket/', include('ticket.urls')),
    path('accounts/', include('users.urls')),
    path('logout/', user_views.logout_user, name='logout'),
    path('all-closed-tickets/', ticket_views.all_closed_tickets, name='all-closed-tickets'),
    
    
]
