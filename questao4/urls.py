from django.urls import path
from questao4 import views


urlpatterns = [
    path('questao4/', views.home, name='questao4'),
]
