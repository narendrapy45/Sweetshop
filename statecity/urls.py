from django.urls import path
from statecity import views

urlpatterns = [
    path('index/',views.index,name='statecityindex' ),
]