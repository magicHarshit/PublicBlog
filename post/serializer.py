from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article, Tag, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('word',)


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
        fields = ('content', 'user',)


