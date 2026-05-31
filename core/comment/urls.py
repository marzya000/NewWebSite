from django.urls import path, include
from blog import views


urlpatterns = [
    path('api/v1/',include('comment.api.v1.urls')),
]
