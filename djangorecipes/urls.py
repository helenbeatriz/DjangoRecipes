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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
    path("accounts/", include("allauth.urls")),
    
]


# Notes for me
#  '/': This route maps to the RecipeListView view, which displays a list of all recipes.
# 'Post/new/': This route maps to the RecipeCreateView view, which displays a form for creating a new Post.
# 'Post/<int:pk>/': This route maps to the RecipeDetailView view, which displays a specific Post based on its primary key (PK) value.
# 'Post/<int:pk>/delete/': This route maps to the RecipeDeleteView view, which displays a confirmation page for deleting a specific Post.