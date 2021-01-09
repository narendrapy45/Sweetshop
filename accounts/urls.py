from django.urls import path
from accounts import views

urlpatterns = [
    path('index/',views.index,name='accountsindex' ),
]