# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)

# from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category

from comment.api.v1.serializers import CommentSerializer
from comment.models import Comment

# from rest_framework import status
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets

# from rest_framework.views import APIView
# from rest_framework.generics import (
#     CreateAPIView,
#     ListAPIView,
#     RetrieveAPIView,
#     RetrieveUpdateAPIView,
#     RetrieveDestroyAPIView,
#     RetrieveUpdateDestroyAPIView,
# )

# from rest_framework.generics import (
#     GenericAPIView,
#     ListAPIView,
#     ListCreateAPIView,
# )

# from rest_framework import mixins
# from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination

"""
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET":    
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
 """


"""
class PostList(APIView):
    ## getting a list of posts and creating new posts 
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request):
        ## retrieving a list of posts
    
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        ## creating a post with provided data
        
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    
"""


"""

class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    ## getting a list of posts and creating new posts 
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    def get(self,request, *args, **kwargs):
        ## retrieving a list of posts
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""


"""
# an instance with ListAPIView
class PostList(ListAPIView):
    ## getting a list of posts and creating new posts 
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
"""


"""
# class PostList(ListCreateAPIView):
#     ## getting a list of posts and creating new posts 
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
"""


"""
class PostDetail(APIView):
    # getting detail of the post and edit plus removing it

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        # retrieving the post data

        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        # editing the post data

        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        # deleting the post object

        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""


"""
class PostDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    # getting detail of the post and edit plus removing it
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""


"""
class PostDetail(RetrieveAPIView):
    # getting detail of the post and edit plus removing it
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

"""

"""
class PostDetail(RetrieveUpdateAPIView):
    # getting detail of the post and edit plus removing it
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
"""


"""
class PostDetail(RetrieveDestroyAPIView):
    # getting detail of the post and edit plus removing it
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
"""

"""
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     # getting detail of the post and edit plus removing it
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
"""


"""
# Example for ViewSet in CBV
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        post_object = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    
    def create(self,request):
        pass

    def update(self,request,pk=None):
        pass

    def partial_update(self,request,pk=None):
        pass

    def destroy(self,request,pk=None):
        pass
"""

"""
## an example SimpleRouter
# class PostModelViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#     @action(methods=["get"],detail=False)
#     def get_ok(self,request):
#         return Response({'detail':'ok'})
"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
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
