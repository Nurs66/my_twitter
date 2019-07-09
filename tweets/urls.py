from .views import (
    RetweetView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView,

    TweetListView,
    TweetDetailView
)
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/')),
    path('search/', TweetListView.as_view(), name='list'),  # /tweet/
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),  # /tweet/1/
    path('create/', TweetCreateView.as_view(), name='create'),  # /tweet/create
    path('<int:pk>/retweet/', RetweetView.as_view(), name='detail'),  # /tweet/1/retweet
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),  # /tweet/1/update/
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),  # /tweet/1/delete/

]
