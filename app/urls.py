from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_alvo/', views.add_alvo, name='add_alvo'),
    path('list/', views.list, name='list'),
    path('list/edit/<int:id>', views.edit_alvo, name='edit'),
    path('list/edit/delete/<int:id>', views.delete, name='delete'),
]
