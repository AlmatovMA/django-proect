from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post

class BaseWiew(TemplateView):
    template_name = "home.html"


class HomePgWiew(TemplateView):
    template_name = "home.html"

class AbautWiew(TemplateView):
    template_name = "abaut.html"


def homePageView(request):
    return HttpResponse("hello word!")


class lsview(ListView):
    model = Post
    template_name = "home.html"

class HomeDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class HomeCreateView(CreateView):
     model = Post
     template_name = 'post_new.html'
     fields = ['title', 'author', 'body']


class HomeUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class HomeDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home.html')
    