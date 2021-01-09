from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from products.forms import CategoryForm,ProductForm
from products.models import Category,ProductModel
from sweetshop import settings
# Create your views here.
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print('....................')
            messages.success(request, 'Category was added successfully!')
            return redirect(addCategory)
    return render(request,'products/addcategory.html',{'form':form})

def viewAllCategories(request):
    category_list = Category.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(category_list, 1)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request,'products/viewallcategories.html',{'categories':categories})


# https://stackoverflow.com/questions/1854237/django-edit-form-based-on-add-form

def editCategory(request,id):
    category = get_object_or_404(Category,id=id)
    form = CategoryForm(request.POST or None,instance=category)
    if request.POST and form.is_valid():
        form.save()
        messages.info(request, 'Category was updated successfully!')
        return redirect(viewAllCategories)
    else:
        return render(request,'products/editcategory.html',{'form':form})

        
def deleteCategory(request,id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    messages.warning(request, 'Category was Deleted.')
    return redirect(viewAllCategories)

def addProductView(request):
    form = ProductForm(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        # image = request.FILES['image']
        # print(image)
        if form.is_valid():
            form.save()
            print('....................')
            messages.success(request, 'Product was added successfully!')
            return redirect(addProductView)
        else:
           messages.warning(request, 'something went wrong.')
           return render(request,'products/addproduct.html',{'form':form})
    else:
        return render(request,'products/addproduct.html',{'form':form})

def viewAllProducts(request):
    products_list = ProductModel.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(products_list, 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request,'products/viewallproducts.html',{'products':products})

def editProduct(request):
    id = request.GET['id']
    product = get_object_or_404(ProductModel,id=id)
    form = ProductForm(request.POST or None,instance=product)
    if request.POST and form.is_valid():
        form.save()
        messages.info(request, 'product was updated successfully!')
        return redirect(viewAllProducts)
    else:
        return render(request,'products/editproduct.html',{'form':form})

def deleteProduct(request):
    id = request.GET['id']
    product = get_object_or_404(ProductModel, pk=id)
    product.delete()
    messages.warning(request, 'product was Deleted.')
    return redirect(viewAllProducts)

