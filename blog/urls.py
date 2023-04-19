from . import views
from django.urls import path, include
from .views import error_404, contact_success
from django.conf.urls import handler500


handler403 = views.error_403
handler500 = 'blog.views.server_error'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('like/<slug:slug>', views.AddLikePost.as_view(), name='post_like'),
    path('post_detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('error_404/', views.error_404, name='error_404'),
    path('403/', handler403, name='403'),
    path('contact_success/', contact_success, name='contact_success'),
    path('400/', views.bad_request, name='bad_request'),
]

