from django.urls import path
from carts import views

urlpatterns = [
   path('index/',views.index,name='cartsindex' ),
]