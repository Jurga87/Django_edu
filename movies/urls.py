from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default view
    path('<int:movienumber>/', views.allmovies_number),
    path('<str:moviename>/', views.allmovies_text,name='movie_url'),
]
