from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('word',)


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.Field(source='user.username')
    # tags = TagSerializer(source='tags')

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'creation_date', 'user', 'tags')
        read_only_fields = ('id', 'creation_date',)


