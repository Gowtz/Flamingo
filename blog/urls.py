from django.urls import path
from .views import add_blog, delete_blog, edit_blog, delete_blog

urlpatterns = [
    path('new/', add_blog, name='new'),
    path('edit/<int:pk>', edit_blog, name='edit'),
    path('delete_post/<int:pk>', delete_blog, name='delete'),
]
