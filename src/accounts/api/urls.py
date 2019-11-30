from django.urls import path
from django.views.generic.base import RedirectView
from tweets.api.views import (
    TweetListApiView,
)
app_name = 'profiles-api'
urlpatterns = [
    path('<str:username>/tweets/', TweetListApiView.as_view(), name="list"),
]
