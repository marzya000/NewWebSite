from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)
import requests
from django_filters.rest_framework import DjangoFilterBackend
from comment.api.v1.serializers import CommentSerializer
from comment.models import Comment
from decouple import config
from django.core.cache import cache
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CategorySerializer, WeatherSerializer
from ...models import Post, Category



class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]# 
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author", "status"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CommentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author", "post"]
    search_fields = ["message"]
    ordering_fields = ["created_date"]
    pagination_class = DefaultPagination



API_KEY = config("OPENWEATHER_API_KEY")

class WeatherAPIView(generics.GenericAPIView):
    serializer_class = WeatherSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = WeatherSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        city = serializer.validated_data["city"]
        cache_key = f"weather_{city}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response({"source": "cache", "data": cached_data})

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "fa"}
        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            return Response({"error": "API error"}, status=500)

        data = response.json()
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }

        cache.set(cache_key, weather_data, timeout=1200)  # 20 دقیقه

        return Response({"source": "api", "data": weather_data})

