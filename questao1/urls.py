from django.urls import path
from questao1 import views


urlpatterns = [
    path('questao1/', views.home, name='questao1'),
]
