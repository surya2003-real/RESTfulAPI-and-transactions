from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login')
            return redirect('login')
    else:    
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def allusers(request):
    context={
        'users':User.objects.all()
    }
    return render(request, 'users/allusers.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')