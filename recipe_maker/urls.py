from django.urls import path
from .views import AddRecipe

app_name = 'recipe_maker'

urlpatterns = [
    path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
]
