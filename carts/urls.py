from django.urls import path
from carts import views

urlpatterns = [
   # path('index/',views.index,name='cartsindex' ),
   path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]