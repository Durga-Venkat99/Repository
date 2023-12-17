from django.urls import path
from  .views import MovieListCreateView
from .views import RapidMovieListView

urlpatterns = [
    path('movies/',MovieListCreateView.as_view(),name='movie_list'),
    # path('rapid_Movie_list/',RapidMovieListView.as_view(),name='rapid_Movie_list')
]