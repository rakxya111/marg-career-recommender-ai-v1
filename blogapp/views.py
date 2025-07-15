from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from blogapp.models import Post , Tag
from django.views.generic import ListView,TemplateView,DetailView,View, CreateView
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from .forms import PostForm , ContactForm , CommentForm ,NewLetterForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(TemplateView):
    template_name = 'marg/base.html'

class AboutView(TemplateView):
    template_name = 'marg/about.html'

class PostListCreateView(LoginRequiredMixin,ListView):  
    model = Post
    template_name = 'marg/Blog/blog.html'
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.filter(
            published_at__isnull=False,
            status='active'
        ).order_by('-published_at')
        
        print(f"Posts found: {queryset.count()}")  # Debug line
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()  # Add the form to context
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 'active'
            post.published_at = timezone.now()
            post.save()

            # Save many-to-many tags manually
            post.tag.set(form.cleaned_data['tag'])

            return redirect(request.path)
        else:
            self.object_list = self.get_queryset() # refetches the post list.
            context = self.get_context_data() # Adds the form with errors to the context.
            context['form'] = form
            return self.render_to_response(context) #Re-renders the page with the error messages.


class PostByTagView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'marg/Blog/BlogList/bloglist.html'
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status='active',
            tag__id=self.kwargs['tag_id'],
        ).order_by['-published_at']
        return query


class ContactView(View):
    template_name = 'marg/contact.html'

    def get(self,request):
        return render(request, self.template_name)
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully Submitted your query . We will contact you soon."
            )
            return redirect(request.path)
        
        else:
            messages.error(
                request,
                "Cannot submit your query. Please make sure all the fields are valid."
            )
        
        return render(
            request,
            self.template_name,
            {"form": form}
        )

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'marg/Blog/Blog-Detail/blog_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull=False,
        status='active')
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['previous_post'] = (
            Post.objects.filter(
                published_at__isnull=False, status='active',
                id__lt=obj.id
            ).order_by('-id')
            .first()
        )

        context['next_post'] = (
            Post.objects.filter(
                published_at__isnull=False, status='active',
                id__gt=obj.id
            ).order_by('id')
            .first()
        )
        return context

class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post_id = request.POST['post']
        if form.is_valid():
            form.save()
            return redirect('post-detail',post_id)
        
        post = Post.objects.get(pk=post_id)
        return render(
            request,
            'marg/Blog/Blog-Detail/blog_detail.html',
            {'post':post, 'form':form} ,
        )
    
class PostSearchView(View):
    template_name = 'marg/Blog/blog.html'

    def get(self,request,*args,**kwargs):
        query = request.GET['query']
        post_list = Post.objects.filter(
            (Q(title__icontains=query) | Q(description__icontains=query))
            & Q(status='active')
            & Q(published_at__isnull=False)
        ).order_by('-published_at')

        page = request.GET.get('page',1)
        paginate_by = 3
        paginator = Paginator(post_list,paginate_by)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        
        return render(
            request,
            self.template_name,
            {'page_obj':posts, 'query': query},
        )

class NewsletterView(View):
   
    def post(self, request):
        is_ajax = request.headers.get("X-Requested-With")
        if is_ajax == "XMLHttpRequest":
            form = NewLetterForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse(
                    {
                        "success": True,
                        "message": "Successfully Subscribed to Newsletter",
                    },
                    status=201,
                )
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "message": "Cannot Subscribe to Newsletter"
                    },
                    status=400,
                )
        else:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Cannot process, Must be an AJAX XMLHttpRequest",
                },
                status=400,
            )   






