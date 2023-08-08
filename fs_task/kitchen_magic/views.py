from typing import Any

# Third-Party Library Imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions

# Local Imports
from .forms import RecipeFilterForm
from .serializers import RecipeSerializer
from . import models


class RecipeDetailView(DetailView):
  model = models.Recipe


class RecipeDeleteView(DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('kitchen-magic-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class RecipeCreateView(permissions.IsAuthenticated, CreateView):
  model = models.Recipe
  fields = ['title', 'ingredients', 'instructions', 'cooking_time']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class RecipeUpdateView(permissions.IsAuthenticated, UpdateView):
  model = models.Recipe
  fields = ['title', 'ingredients', 'instructions', 'cooking_time']

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

# Filter out Recipes table by creating querysets
class RecipeFilterListView(ListView):
  model = models.Recipe
  template_name = 'kitchen_magic/home.html'
  context_object_name = 'recipes'
  ordering = ['-updated_at']

  def get_queryset(self):
    queryset = super().get_queryset()
    form = RecipeFilterForm(self.request.GET)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        ingredients = form.cleaned_data.get('ingredients')
        cooking_time = form.cleaned_data['cooking_time']

        if title:
            queryset = queryset.filter(title__icontains=title)
        if ingredients:
            queryset = queryset.filter(ingredients__icontains=ingredients)
        if cooking_time:
            queryset = models.Recipe.objects.filter(cooking_time=cooking_time)
            
    return queryset

def homepage(request):
    recipes = RecipeFilterListView.as_view()(request)
    return render(request, 'kitchen_magic/home.html', {'recipes': recipes.context_data['recipes'], 'form': RecipeFilterForm()})

# DRF viewset
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serlaizer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    