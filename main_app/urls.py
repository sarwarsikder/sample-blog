from django.urls import path
from .views import home, about, post, details

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('post', post, name='post'),
    path('details/<int:pk>/', details, name='details'),    # Add other URL patterns if needed
]
