from django.urls import path
from django.views.generic.base import RedirectView
from .views import (TweetDetailView, TweetListView,
                    TweetCreateView, TweetUpdateView,
                    TweetDeleteView, RetweetView)
app_name = 'tweet'
urlpatterns = [
    path('', RedirectView.as_view(url='/'), name="list"),
    path('<int:pk>/', TweetDetailView.as_view(), name="detail"),
    path('<int:pk>/retweet/', RetweetView.as_view(), name="retweet"),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/edit', TweetUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', TweetDeleteView.as_view(), name="delete"),
]
