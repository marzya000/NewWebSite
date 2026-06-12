from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentSerializer
from ...models import Comment
from .permissions import IsOwnerOrReadOnly


class CommentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()