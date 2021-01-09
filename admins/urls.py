from django.urls import path
from admins import views

urlpatterns = [
    path('index/',views.index,name='adminsindex' ),
]