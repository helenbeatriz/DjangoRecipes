from django.urls import path
from .views import AddRecipe, Recipes, RecipeDetail

app_name = "recipe_maker"

urlpatterns = [
    path("add_recipe/", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail")
]

