from .views import (
    RetweetAPIView,
    TweetListAPIView,
    TweetCreateAPIView,
    LikeToggleAPIView,
)

from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url='/')),
    path('', TweetListAPIView.as_view(), name='list'),  # /api/tweet/
    path('create/', TweetCreateAPIView.as_view(), name='create'), # /api/tweet/create/
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like-toggle'),
    path('<int:pk>/retweet/', RetweetAPIView.as_view(), name='retweet'),#/api/tweet/id/retweet
]
