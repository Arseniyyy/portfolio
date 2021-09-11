from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects_index, name='main_page'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
