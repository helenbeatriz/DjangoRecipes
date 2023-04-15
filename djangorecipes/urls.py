"""djangorecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipe_maker.views import RecipeCreateView, Recipes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path("accounts/", include("allauth.urls")),
    path("", include("recipe_maker.urls"), name="recipe_maker-urls"),
    path('add_recipe/', RecipeCreateView.as_view(), name='add_recipe'),
    path('recipes/', Recipes.as_view(), name='recipes'),

    ]


# Notes for me
# 'Post/<int:pk>/': This route maps to the RecipeDetailViewView view, which displays a specific Post based on its primary key (PK) value.
# 'Post/<int:pk>/delete/': This route maps to the RecipeDeleteView view, which displays a confirmation page for deleting a specific Post.