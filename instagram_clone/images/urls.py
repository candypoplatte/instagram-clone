from django.urls import path

from instagram_clone.images import views

app_name = 'images'
urlpatterns = [
    path(
        route='all/',
        view=views.ListAllImages.as_view(),
        name="all-images"
    ),
    path(
        route='comments/',
        view=views.ListAllComments.as_view(),
        name="all-comments"
    ),
    path(
        route='likes/',
        view=views.ListAllLikes.as_view(),
        name="all-likes"
    ),
]
