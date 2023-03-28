from django.views import View
from django.shortcuts import render

class Recipes(View):
    def get(self, request):
        # Your view logic here
        return render(request, 'recipe_maker/recipes.html')