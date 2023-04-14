from django.urls import path
from .views import AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe

app_name = "recipe_maker"

urlpatterns = [
    path("add_recipe/", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe",)


]

