from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article, Tag, Comment, Vote, FavoriteArticle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name','id',)


class ArticleSerializer(serializers.ModelSerializer):

    user_id = serializers.Field(source='user.id')
    user = serializers.Field(source='user.username')
    tag_details = TagSerializer(source='tags', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'creation_date', 'user', 'tags','tag_details','user_id')
        read_only_fields = ('id', 'creation_date',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')

    class Meta:
        model = Comment
        fields = ('content', 'user','id',)

class VoteSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')
    class Meta:
        model = Vote
        fields = ('user', 'article', 'vote_type','id')


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('points',)


class FavoriteArticleSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='user.username')

    class Meta:
        model = FavoriteArticle
        fields = ('article','user',)
