from django.urls import path
from .views import Recipes

urlpatterns = [
    path('', Recipes, name='recipes')
]
