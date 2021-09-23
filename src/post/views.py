from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from post.models import Post, PostView, Like, Comment
# Create your views here.


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'autor',
        'slug',
    )


class PostDeleteView(DeleteView):
    model = Post
