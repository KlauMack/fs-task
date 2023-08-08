from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet
from . import views

# Registering a viewset for a DRF API
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', views.homepage, name="kitchen-magic-home"),
    path('kitchen_magic/<int:pk>', views.RecipeDetailView.as_view(), name="kitchen-magic-detail"),
    path('kitchen_magic/create', views.RecipeCreateView.as_view(), name="kitchen-magic-create"),
    path('kitchen_magic/<int:pk>/update', views.RecipeUpdateView.as_view(), name="kitchen-magic-update"),
    path('kitchen_magic/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="kitchen-magic-delete"),
    path('api/', include(router.urls)),
]
