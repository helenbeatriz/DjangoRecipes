from django.apps import AppConfig

class RecipeMakerConfig(AppConfig):
    # Configuration class for the Recipe Maker app
    default_auto_field = "django.db.models.BigAutoField"  # specifies the default primary key type
    name = "recipe_maker"  # name of the app
