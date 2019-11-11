from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (DetailView, ListView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
# Create your views here.


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin,
                      CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    login_url = '/admin/'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy('tweet:list')
    template_name = 'tweets/delete_confirm.html'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    login_url = '/admin/'


class TweetDetailView(DetailView):
    template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = 'tweets/list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs
