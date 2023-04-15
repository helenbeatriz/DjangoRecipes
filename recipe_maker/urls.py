from django.urls import path
from .views import RecipeCreateView, Recipes, RecipeDetailView, RecipeDeleteView, RecipeUpdateView

# Set an app name for reverse URL lookups
app_name = "recipe_maker"

# Define the urlpatterns list with the paths for the views
urlpatterns = [
    # Path for creating a new recipe
    path("add_recipe/", RecipeCreateView.as_view(), name="add_recipe"),
    
    # Path for listing all the recipes
    path("recipes/", Recipes.as_view(), name="recipes"),
    
    # Path for displaying a recipe's details
    path("<slug:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    
    # Path for deleting a recipe
    path("delete/<int:pk>/", RecipeDeleteView.as_view(), name="delete_recipe"),
    
    # Path for editing a recipe
    path("edit/<slug:pk>/", RecipeUpdateView.as_view(), name="edit_recipe",)
]
