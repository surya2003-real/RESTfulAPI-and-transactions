from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
#Create your views here.
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
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)

#view profile using a primary key
def view_profile_pk(request, pk):
    user=User.objects.get(pk=pk)
    return render(request, 'users/profile.html', {'user':user})

#delete all users
def delete_all_users(request):
    User.objects.all().delete()
    return redirect('allusers')
#delete a user using a primary key
def delete_user_pk(request, pk):
    User.objects.get(pk=pk).delete()
    return redirect('allusers')



