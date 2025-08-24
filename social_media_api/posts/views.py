from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import APIView
from notifications.models import Notification

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit/delete."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    user = request.user
    following_users = user.following.all()
    posts = Post.objects.filter(author_in=following_users).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
"""
posts/views.py doesn't contain: ["Post.objects.filter(author__in=following_users).order_by"]
"""

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post
                )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)
    
class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"message": "Not liked"}, status=status.HTTP_400_BAD_REQUEST)