from rest_framework import viewsets

from api.serializers import PostModelSerializer
from posts.models import Post

class PostViewSet(viewsets.ModelViewSet):


    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostModelSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

