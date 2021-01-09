from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'this is carts Html page'
    return render(request,'carts/index.html',{'title':title})