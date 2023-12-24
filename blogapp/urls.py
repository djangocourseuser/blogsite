# blogapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
]
