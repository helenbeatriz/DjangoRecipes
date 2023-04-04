from . import views
from django.urls import path, include
from .views import contact, contact_success


# from .views import error_404

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('error_404/', views.error_404, name='error_404'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]

