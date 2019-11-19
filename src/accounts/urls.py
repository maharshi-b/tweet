from django.urls import path
from django.views.generic.base import RedirectView
from .views import UserDetailView, UserFollowView
app_name = 'profiles'
urlpatterns = [

    path('<str:username>/', UserDetailView.as_view(), name="detail"),
    path('<str:username>/follow', UserFollowView.as_view(), name="follow"),
    # path('create/', TweetCreateApiView.as_view(), name='create'),
    # path('<int:pk>/edit', TweetUpdateView.as_view(), name="update"),
    # path('<int:pk>/delete', TweetDeleteView.as_view(), name="delete"),
]
