from django.urls import path
from accounts import views

urlpatterns = [
    path('index/',views.index,name='accountsindex' ),
    path('signup/',views.signupView,name='signup'),
    path('signin/',views.signInView,name='signin'),
    path('signout/',views.signOutView,name='signout'),
]