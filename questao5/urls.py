from django.urls import path
from questao5 import views


urlpatterns = [
    path('questao5/', views.home, name='questao5'),
]
