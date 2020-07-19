from django.urls import path 
from registration.views import Login_View, SignUpView
from . import views

urlpatterns = [
    path('login/',views.Login_View.as_view() , name='login'),
    path('signup/',views.SignUpView.as_view() , name='signup')
]