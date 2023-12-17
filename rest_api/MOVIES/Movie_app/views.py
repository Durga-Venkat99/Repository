from django.shortcuts import render
from django.views import View
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
import requests

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

# class RapidMovieListView(View):
#     def get(self, request):
#         url = "https://imdb8.p.rapidapi.com/auto-complete"
#         querystring = {"q": "game"}

#         headers = {
#             "X-RapidAPI-Key": "898b8efe65msh360ddeb2d77f0e9p1fb13ejsnb3c4054a2899",
#             "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
#         }

#         response = requests.get(url, headers=headers, params=querystring)

#         print(response.json())
#         return render(request, 'movie_list.html', {'movies': response.json()})
