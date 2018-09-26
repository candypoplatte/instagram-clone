from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram_clone.images import serializers
from instagram_clone.images.models import Image, Like


class Feed(APIView):
    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()

        images = []
        for following_user in following_users:
            following_user_images = following_user.images.all()[:2]
            images += following_user_images

        sorted_images = sorted(images, key=lambda image: image.created, reverse=True)
        serializer = serializers.ImageSerializer(sorted_images, many=True)
        return Response(data=serializer.data)


class LikeImage(APIView):
    def post(self, request, image_id, format=None):
        user = request.user
        image = get_object_or_404(
            Image,
            pk=image_id
        )
        Like.objects.create(
            creator=user,
            image=image
        )
        return Response(status=201)
