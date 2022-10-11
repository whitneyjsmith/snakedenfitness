# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} successfully created')
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    # check if logged in
    #
    #
    return render(request, 'users/profile.html', {})
