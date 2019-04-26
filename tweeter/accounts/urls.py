from .views import (
    UserDetailView,
    UserFollowView,
)
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('<username>/', UserDetailView.as_view(), name='detail'),
    path('<username>/follow', UserFollowView.as_view(), name='follow'),
]
