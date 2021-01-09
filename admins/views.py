from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'this is Admins Html page'
    return render(request,'admin/index.html',{'title':title})