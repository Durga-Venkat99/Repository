from django.db import models

# class Movie(models.Model):
#     title = models.CharField(max_length=255)
#     director = models.CharField(max_length=255)
#     release_date = models.DateField()
#     description = models.TextField()
    
#     def __str__(self):
#         return self.title

class MovieDate(models.Model):
    # movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.movie.title} - {self.date}"