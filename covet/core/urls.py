from django.contrib.auth import views as auth_views #djangos built in login authenticator for login url (custom view not needed) 

from django.urls import path 

from . import views
from .forms import LoginForm    #passing in our custom login form 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("contact/", views.contact, name='contact'),   #contact us page
    path('signup/', views.signup, name='signup'),
    path('legal/', views.legal, name="legal"),
    path('about', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'), #redirect to a custom login form...otherwise django doesnt know what to get
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # default django logout
]
