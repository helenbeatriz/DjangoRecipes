from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm

# Display a list of recipes
class Recipes(ListView):
    template_name = "recipes.html"
    model = Recipe
    context_object_name = "recipes"


# Display the details of a recipe
class RecipeDetailView(DetailView):
    template_name = "recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"

# Add a new recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        # Set the user of the recipe to the current user
        form.instance.user = self.request.user
        return super(RecipeCreateView, self).form_valid(form)

# Delete a recipe
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "recipe_confirm_delete.html"
    model = Recipe
    context_object_name = "recipe"
    success_url = "/recipes/"

    def test_func(self):
        # Check if the current user is the user who created the recipe
        return self.request.user == self.get_object().user

# Edit a recipe
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a recipe"""
    template_name = 'edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'
    
    def test_func(self):
        # Check if the current user is the user who created the recipe
        return self.request.user == self.get_object().user 

