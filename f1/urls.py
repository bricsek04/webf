from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drivers/<int:pk>/delete/', views.delete_driver, name='driver-delete'),
    path('drivers/<int:pk>/assign/', views.assign_team, name='assign-team'),
]