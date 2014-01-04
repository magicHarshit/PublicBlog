from .models import Article, Tag, Comment, Vote
from .serializer import ArticleSerializer, TagSerializer, UserSerializer, CommentSerializer, VoteSerializer
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


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
            queryset = queryset.filter(name__icontains=query)
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


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        article_id = self.kwargs.get('article_id')
        return queryset.filter(post_id= article_id)

    def pre_save(self, obj):
        article_id = self.kwargs.get('article_id')
        obj.post_id = article_id
        obj.user = self.request.user


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def pre_save(self,obj):
        obj.user = self.request.user

    def get_queryset(self):
        queryset = Vote.objects.all()
        query = self.request.QUERY_PARAMS.get('q', None)
        if query is not None:
            queryset = queryset.filter(article_id=query, user=self.request.user)
        return queryset


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)




