from django.forms import ModelForm
from products.models import Category,ProductModel

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        def __init__(self, *args, **kwargs):
            # first call parent's constructor
            super(CategoryForm, self).__init__(*args, **kwargs)
            # there's a `fields` property now
            self.fields['name'].required = True

class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name','price','category','image','desc']
