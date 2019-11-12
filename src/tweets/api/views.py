from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweet


class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        queryset = Tweet.objects.all()
        return queryset
