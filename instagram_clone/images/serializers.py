from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    like_set = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
            'creator',
            'comment_set',
            'like_set',
        )
