from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "meal_type",
        "cuisine_types",
        "calories",
        "posted_date",
    )

    list_filter = ("meal_type",)
