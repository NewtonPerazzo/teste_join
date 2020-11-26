from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('list/', include('questao1.urls')),
    path('list/', include('questao5.urls')),
    path('list/', include('questao4.urls')),
]
