from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Recipe table
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.DurationField(default='HH:MM:SS')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Each object has its own unique integer
    def get_absolute_url(self):
        return reverse("kitchen-magic-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
