#=========== 31/07/2024 ------------- fernando flores ===
# estos links se corresponden con la rta de la url 
# =======================================================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # otras rutas aquí
]
