from rest_framework import serializers
from .models import Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('word',)


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.Field(source='user.username')
    tags = TagSerializer(source='tags', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'creation_date', 'user', 'tags')
        read_only_fields = ('id', 'creation_date')


