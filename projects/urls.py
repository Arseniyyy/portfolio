from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
