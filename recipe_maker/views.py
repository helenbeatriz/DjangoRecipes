from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    template_name = "recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(instructions__icontains=query)
                | Q(cuisine_types__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes



class RecipeDetail(DetailView):
    template_name = "recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"



class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)

 
