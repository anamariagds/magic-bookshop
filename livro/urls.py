from django.urls import path
from . import views

urlpatterns = [
    path('ver_livros/', views.ver_livros, name='ver_livros'),
    path('romance/', views.romance, name='romance'),
    path('ficcao/', views.ficcao, name='ficcao'),
    path('terror/', views.terror, name='terror'),
]