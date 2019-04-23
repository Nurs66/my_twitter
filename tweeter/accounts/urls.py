from .views import (
    UserDetailView,
)
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('<username>/', UserDetailView.as_view(), name='detail'),
]
