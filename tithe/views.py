# -*- coding: utf-8 -*-
from django.shortcuts import redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import TemplateView
from form import OfferingForm
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'tithe/base.html', context=None)

# Create other options here.
@login_required
def offerings_add(request):
    form = OfferingForm()
    return render(request, 'tithe/offerings_add.html', {'form': form})
def add(tithes,combinedoffering,churchbuilding,conference,localchurch,funds):
     return tithes+combinedoffering+churchbuilding+conference+localchurch+funds

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile/password/')
        else:
            return redirect('account/change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change_password.html', args)

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html', args)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)  