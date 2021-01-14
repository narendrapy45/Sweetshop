from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .forms import UserRegistrationForm,UserLogInForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    title = 'this is Accounts Html page'
    return render(request,'accounts/index.html',{'title':title})

def signupView(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:

                firstName = form.cleaned_data['first_name']
                lastName = form.cleaned_data['first_name']
                Email = form.cleaned_data['email_id']
                userName = form.cleaned_data['user_name']
                contactNo = form.cleaned_data['contact_no']
                country = form.cleaned_data['country']
                birth_date = form.cleaned_data['birth_date']
                password = form.cleaned_data['password']
                try:
                    user = User.objects.create_user(username=userName,password=password, email=Email,
                                                    first_name=firstName, last_name=lastName)
                    user.save()
                except:
                    messages.warning(request,'something Went Wrong Register can not be done')
                    return redirect('signup')
                
                try:
                    profile=Profile(mobile_no=contactNo,user_id=user.id,country=country,birth_date=birth_date)
                    print('......')
                    profile.save()
                
                    
                except:
                    messages.warning(request,'something Went Wrong Register can not be done')
                    return redirect('signup')

                messages.info(request,'Registered Successfully please please login ')
                return render(request,'home.html')
            except:
                messages.warning(request,'phone number or mail already exists ')
                return redirect('signup')
    return render(request,'accounts/signup.html',{'form':form})

def signInView(request):
    form = UserLogInForm(request.POST or None)

    if request.method=='POST':
        if form.is_valid():
            
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            try:
                user = auth.authenticate(username=username, password=password)
            except:
                messages.warning(request, 'invalid credentials')
                return redirect('signin')
            else:
                if user is not None:
                    auth.login(request, user)
                    messages.info(request, f"welcome '{user.first_name}'")
                    return render(request,'home.html')
        messages.warning(request,'invalid Credentials')
        return redirect('signin')
    return render(request,'accounts/signin.html',{'form':form})

def signOutView(request):
    auth.logout(request)
    messages.info(request, "Success fully logged out")
    return render(request,'home.html')