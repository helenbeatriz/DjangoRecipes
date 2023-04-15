from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe

class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""

    # Defines the model to use for the form
    class Meta:
        model = Recipe

        # Defines the fields to include in the form
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "meal_type",
            "cuisine_types",
            "calories",
        ]

        # Defines the widgets to use for the "ingredients" and "instructions" fields
        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        # Defines the widget to use for the "description" field
        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        # Defines the labels to use for the form fields
        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
        }
