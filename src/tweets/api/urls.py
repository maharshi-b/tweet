from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    TweetListApiView
)
app_name = 'tweet-api'
urlpatterns = [
    path('', TweetListApiView.as_view(), name="api-list"),
    # path('<int:pk>/', TweetDetailView.as_view(), name="detail"),
    # path('create/', TweetCreateView.as_view(), name='create'),
    # path('<int:pk>/edit', TweetUpdateView.as_view(), name="update"),
    # path('<int:pk>/delete', TweetDeleteView.as_view(), name="delete"),
]