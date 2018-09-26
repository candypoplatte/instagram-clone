from rest_framework.response import Response
from rest_framework.views import APIView

from instagram_clone.images import serializers


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
