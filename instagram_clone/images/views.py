from rest_framework.views import APIView
from rest_framework.response import Response

from instagram_clone.images.models import Image, Comment, Like
from instagram_clone.images import serializers


class ListAllImages(APIView):
    def get(self, request, format=None):
        all_images = Image.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)
        return Response(data=serializer.data)


class ListAllComments(APIView):
    def get(self, request, format=None):
        all_comments = Comment.objects.all()
        serializer = serializers.CommentSerializer(all_comments, many=True)
        return Response(data=serializer.data)


class ListAllLikes(APIView):
    def get(self, request, format=None):
        all_likes = Like.objects.all()
        serializer = serializers.LikeSerializer(all_likes, many=True)
        return Response(data=serializer.data)
