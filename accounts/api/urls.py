from tweets.api.views import (
    TweetListAPIView,
)

from django.urls import path


urlpatterns = [
    path('<username>/tweet/', TweetListAPIView.as_view(), name='list'),  # /api/tweet/
]
