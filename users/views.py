from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import registration_form

# Create your views here.
def registration(request):
        if(request.method=='POST'):
            form = registration_form(request.POST)
            if(form.is_valid()):
                form.save()
                username = form.cleaned_data['username']
                messages.success(request,f'Account created for {username}!')
                form = registration_form()
                return redirect('blog:home_page')
        else:
            form = registration_form()
        return render(request,'users/registration.html',{'form': form})

@login_required
def profile(request):

    return render(request,'users/profile.html')
