# Importing required modules
from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Defining choice fields
DIFFICULTY_LEVEL = (("easy", "Easy"), ("Medium", "Medium"), ("hard", "Hard"))
CUISINE_TYPES = (
    ("african", "African"),
    ("american", "American"),
    ("asian", "Asian"),
    ("middle_eastern", "Middle Eastern"),
    ("brazilian", "Brazilian"),
    ("indian", "Indian"),
    ("european", "European"),
)

# Creating a Recipe model to manage and create recipes
class Recipe(models.Model):
    # Defining fields for Recipe model
    user = models.ForeignKey(User, related_name="recipe_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False, default="")
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    meal_type = models.CharField(max_length=50, choices=DIFFICULTY_LEVEL, default="easy")
    cuisine_types = models.CharField(
        max_length=50, choices=CUISINE_TYPES, default="african"
    )
    calories = models.IntegerField()
    posted_date = models.DateTimeField(auto_now=True)

    # Defining meta options for Recipe model
    class Meta:
        ordering = ["-posted_date"]

    # Defining a string representation for Recipe model
    def __str__(self):
        return str(self.title)
