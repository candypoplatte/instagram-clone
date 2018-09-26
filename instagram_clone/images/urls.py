from django.urls import path

from instagram_clone.images import views

app_name = 'images'
urlpatterns = [
    path(
        route='',
        view=views.Feed.as_view(),
        name="feeds"
    ),
    path(
        route='<int:image_id>/like',
        view=views.LikeImage.as_view(),
        name="like-image"
    ),
]
