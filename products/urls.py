from django.urls import path
from products import views

urlpatterns = [
   path('addcategory/',views.addCategory,name='addcategory'),
   path('viewallcategories/',views.viewAllCategories,name='viewallcategories'),
   path('editcategory/<int:id>',views.editCategory,name='editcategory'),
   path('deletecategory/<int:id>',views.deleteCategory,name='deletecategory'),

   path('addproduct/',views.addProductView,name='addproduct'),
   path('viewallproducts/',views.viewAllProducts,name='viewallproducts'),
   path('editproduct/',views.editProduct,name='editproduct'),
   path('deleteproduct/',views.deleteProduct,name='deleteproduct'),
]