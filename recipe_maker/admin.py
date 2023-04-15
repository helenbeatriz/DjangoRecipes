# Importing the admin module and the Recipe model from the current package
from django.contrib import admin
from .models import Recipe

# Registering the Recipe model with the admin site
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Setting the fields to be displayed in the admin interface
    list_display = (
        "title",
        "description",
        "meal_type",
        "cuisine_types",
        "calories",
        "posted_date",
    )
    
    # Adding a filter to the admin interface for the meal_type field
    list_filter = ("meal_type",)
