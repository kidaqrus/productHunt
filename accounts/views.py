from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'username has already been taken'})
            except User.DoesNotExist:
            
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)    
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'passwords must match'})
            
          
    else:
        #User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    
    if request.method == 'POST':
         
                #to check if user has already sign up
                user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
                # this takes us to the login page after the check has been made
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'accounts/login.html', {'error':'username or password is incorrect'})

    else:
         return render(request, 'accounts/login.html') 
           
                
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # TODO-  need to route to homepage
        return redirect('home')
    
    # and dont forget to logout
    return render(request, 'accounts/logout.html')
# Create your views here.
