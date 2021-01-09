from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'this is Statecity Html page'
    return render(request,'statecity/index.html',{'title':title})