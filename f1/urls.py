from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drivers/', views.driver_list, name='driver-list'),
    path('drivers/add/', views.driver_add, name='driver-add'),
    path('drivers/<int:pk>/edit/', views.driver_edit, name='driver-edit'),
    path('drivers/<int:pk>/delete/', views.driver_delete, name='driver-delete'),

    path('teams/', views.team_list, name='team-list'),
    path('teams/add/', views.team_add, name='team-add'),
    path('teams/<int:pk>/edit/', views.team_edit, name='team-edit'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team-delete'),
]