from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import filters

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend , filters.OrderingFilter]
    filterset_fields = ['genre', 'release_date']
    ordering_fields = ['release_date', 'duration']

