from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from kitchen_magic import models

def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account is created, please login.")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
# User must be looged in to access the profile url
@method_decorator(login_required, name='dispatch')
class UserRecipeListView(ListView):
  model = models.Recipe
  template_name = 'users/profile.html'
  context_object_name = 'recipes'
  ordering = ['-updated_at']
