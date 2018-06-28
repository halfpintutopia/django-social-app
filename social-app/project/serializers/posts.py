from rest_framework import serializers
from project.feed.models import Post


# class PostSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     user = serializers.CharField(read_only=True)
#     content = serializers.CharField(required=True)
#     created = serializers.DateTimeField(read_only=True)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created']
        read_only_fields = ['user']
