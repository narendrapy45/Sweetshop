from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'this is Accounts Html page'
    return render(request,'accounts/index.html',{'title':title})