

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('blog/',views.blog,name='blog'),
    path('addpost/',views.addpost,name='addpost'),
    path('blog_details/<int:id>',views.blog_details,name='blog_details'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post'),
    path('edit_post/<int:id>',views.edit_post,name='edit_post'),
    path('search/',views.search,name='search')
    
    
]
