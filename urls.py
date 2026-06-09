from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_record, name='add_record'),
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),
    path('toggle/<int:pk>/', views.toggle_status, name='toggle_status'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
]