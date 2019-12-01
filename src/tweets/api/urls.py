from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    TweetListApiView, TweetCreateApiView, RetweetAPIView, LikeToggleAPIView
)
app_name = 'tweet-api'
urlpatterns = [
    path('', TweetListApiView.as_view(), name="list"),
    path('<int:pk>/retweet/', RetweetAPIView.as_view(), name="retweet"),
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name="like"),
    path('create/', TweetCreateApiView.as_view(), name='create'),
    # path('<int:pk>/edit', TweetUpdateView.as_view(), name="update"),
    # path('<int:pk>/delete', TweetDeleteView.as_view(), name="delete"),
]
