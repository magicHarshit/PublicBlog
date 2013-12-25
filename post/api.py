from .models import Article, Tag
from .serializer import ArticleSerializer, TagSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class TagList(generics.ListAPIView):
    model = Tag
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        This view should return a list of
        if q, all tags that contain q
        else, all tags
        """
        queryset = Tag.objects.all()
        query = self.request.QUERY_PARAMS.get('q', None)
        if query is not None:
            queryset = queryset.filter(word__icontains=query)
        return queryset


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tag instance.
    """
    model = Tag
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

