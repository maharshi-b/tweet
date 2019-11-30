from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultsPagination
from rest_framework.views import APIView
from rest_framework.response import Response


class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        if tweet_qs.exists() and tweet_qs.count() == 1:
            if request.user.is_authenticated:
                new_tweet = Tweet.objects.retweet(
                    request.user, tweet_qs.first())
                if new_tweet is not None:
                    data = TweetModelSerializer(new_tweet).data
                    return Response(data)
                return Response("Can't again", status=400)
            return Response("Not allowed", status=400)
        return Response("Not exists", status=400)


class TweetCreateApiView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get('username')
        if requested_user:
            qs = Tweet.objects.filter(
                user__username=requested_user).order_by("-timestamp")

        else:
            following_users = self.request.user.profile.get_following()
            qs = Tweet.objects.filter(
                Q(user__in=following_users) |
                Q(user=self.request.user)).order_by("-timestamp")
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs
