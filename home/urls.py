from django.urls import path

from . import views
from notes import views as notesview

urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('signup/', notesview.signup_view, name='signup'),

]