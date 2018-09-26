from rest_framework.views import APIView
from rest_framework.response import Response

from instagram_clone.images.models import Image
from instagram_clone.images import serializers


class ListAllImages(APIView):
    def get(self, request, format=None):
        all_images = Image.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)
        return Response(data=serializer.data)
