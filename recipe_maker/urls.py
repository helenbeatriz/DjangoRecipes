from django.views.generic import (CreateView, ListView)
from django.urls import path
from .views import AddRecipe, Recipes

app_name = 'recipe_maker'

urlpatterns = [
    path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
    path('recipes/', Recipes.as_view(), name='recipes'),

]
