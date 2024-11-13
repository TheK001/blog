from django.urls import path
from . import views 


urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('add/', views.add_blogs, name="add_blogs"),
    path('update/<int:pk>/', views.update_blog, name="update_blogs"),
    path('delete/<int:pk>/', views.delete_blog, name="delete_blogs"),
]


