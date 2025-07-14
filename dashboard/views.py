from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blogapp.models import Post, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .forms import PostForm, TagForm
from django.utils import timezone



class DashboardView(LoginRequiredMixin, ListView):  # Renamed from dashboardView
    model = Post 
    template_name = 'marg/Dashboard/dashboard.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=False, status="active").order_by("-published_at")


class PostListView(LoginRequiredMixin, ListView):  # Renamed from PostlistView
    model = Post
    template_name = 'marg/Dashboard/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=False, status='active').order_by('-published_at')


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post-list-view')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'marg/Dashboard/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'marg/Dashboard/post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('dash-post-detail', kwargs={"pk": self.object.pk})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'marg/Dashboard/post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('dash-post-detail', kwargs={"pk": self.object.pk})
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostPublishView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.save()
        return redirect("post-list-view")


class InactivePostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'marg/Dashboard/inactive_post_list.html' 
    context_object_name = 'posts1'          

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True, status='in_active')


class MakeActiveView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status='in_active')
        post.status = 'active'
        post.published_at = timezone.now()
        post.save()
        return redirect('inactive-post-view')


class DeActiveView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, published_at__isnull=False, status='active')
        post.published_at = None
        post.status = 'in_active'
        post.save()
        return redirect('inactive-post-view')


class TagListView(LoginRequiredMixin, ListView):  # Renamed from TaglistView
    model = Tag
    template_name = 'marg/Dashboard/tags.html'
    context_object_name = 'tags'


class TagDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return redirect('tag-list')


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'marg/Dashboard/create_tag.html'
    form_class = TagForm

    def get_success_url(self):
        return reverse_lazy('tag-list')


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "marg/Dashboard/create_tag.html"
    form_class = TagForm

    def get_success_url(self):
        return reverse_lazy("tag-list")
