from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from blogapp.models import Post , Tag , Comment
from django.views.generic import ListView,TemplateView,DetailView,View, UpdateView , FormView
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from .forms import PostForm , ContactForm , CommentForm ,NewLetterForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'marg/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(
        published_at__isnull=False,
        status='active'
        ).order_by("-published_at") [:4]
    

class AboutView(TemplateView):
    template_name = 'marg/about.html'



class PostListCreateView(LoginRequiredMixin, ListView):  
    model = Post
    template_name = 'marg/Blog/blog.html'
    context_object_name = "page_obj"  # Changed from "posts" to "page_obj"


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
        context['query'] = ''  # Add empty query for template consistency
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


class PostByTagView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'marg/Blog/blog.html'
    context_object_name = "page_obj"

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(
            published_at__isnull=False,
            status='active',
            tag__id=self.kwargs['tag_id'],
        ).order_by('-published_at')



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



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'marg/Blog/Blog-Detail/blog_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(published_at__isnull=False, status='active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()

        # Fetch the current user's comment (if any) on this post
        user_comment = Comment.objects.filter(post=obj, user=self.request.user).first()

        # Pass it to the context
        context['user_comment'] = user_comment
        context['form'] = CommentForm(instance=user_comment) if user_comment else CommentForm()

        context['latest_post'] = (
            Post.objects.filter(
                published_at__isnull=False , status='active'
            ).order_by('-published_at')[:5]
        )

        context['tags'] = Tag.objects.all()[:8]

        # For next/previous post navigation
        context['previous_post'] = (
            Post.objects.filter(
                published_at__isnull=False, status='active',
                id__lt=obj.id
            ).order_by('-id').first()
        )
        context['next_post'] = (
            Post.objects.filter(
                published_at__isnull=False, status='active',
                id__gt=obj.id
            ).order_by('id').first()
        )
        return context



class CommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        # Fetch current user's comment on this post (if exists)
        existing_comment = Comment.objects.filter(post=post, user=request.user).first()

        # --- CREATE ---
        if action == "create":
            if existing_comment:
                messages.error(request, "You have already commented on this post.")
            else:
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = request.user
                    comment.post = post
                    comment.save()
                    messages.success(request, "Comment added successfully!")
                else:
                    messages.error(request, "Please correct the errors in your comment.")

        # --- UPDATE ---
        elif action == "update":
            if not existing_comment:
                messages.error(request, "You haven't commented yet.")
            else:
                form = CommentForm(request.POST, request.FILES, instance=existing_comment)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Comment updated successfully!")
                else:
                    messages.error(request, "Error updating comment.")

        # --- DELETE ---
        elif action == "delete":
            if not existing_comment:
                messages.error(request, "No comment found to delete.")
            else:
                existing_comment.delete()
                messages.success(request, "Comment deleted.")

        else:
            messages.error(request, "Invalid action.")

        return redirect("post-detail", pk=post.pk)



  
class PostSearchView(View):
    template_name = 'marg/Blog/blog.html'

    def get(self, request, *args, **kwargs):
        # Use .get() with default to avoid MultiValueDictKeyError
        query = request.GET.get('query', '').strip()

        # If no query, show all posts (same as PostListCreateView)
        if query:
            post_list = Post.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query),
                status='active',
                published_at__isnull=False
            ).order_by('-published_at')
        else:
            # Show all posts when no search query
            post_list = Post.objects.filter(
                status='active',
                published_at__isnull=False
            ).order_by('-published_at')

        paginator = Paginator(post_list, 3)
        page = request.GET.get('page', 1)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        return render(
            request,
            self.template_name,
            {
                'page_obj': posts,
                'query': query,
                'form': PostForm(),
            }
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






