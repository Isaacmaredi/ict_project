from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User

from django.template import RequestContext

# Create your views here.
def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(username)
        
        if password == password2:
            
            if User.objects.filter(username = username).exists():
                messages.error(request, 'That user name already exists')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists() and  User.objects.exclude(email=''):
                    messages.error(request,'That email is already taken')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request, f'User {username} has been succesfully registered!')
                    return redirect('profiles:profile-admin')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')      
    else:
        return render (request,'accounts/register.html')
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            context= {
                username:"username"
            } 
        
            messages.success(request, f'Welcome, {user.first_name}! You are now logged in')
            return redirect('profiles:profile-list')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect ('accounts:login')
        # return HttpResponseRedirect(settings.LOGIN_URL)
    
class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy ('accounts:password-change-done')
    
class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    
