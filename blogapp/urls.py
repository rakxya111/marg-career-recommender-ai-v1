from django.urls import path
from blogapp import views

urlpatterns = [
    
    path('', views.HomeView.as_view(), name='home'),
    path('post-list/', views.PostListCreateView.as_view(), name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('post-by-tag/<int:tag_id>/',views.PostByTagView.as_view(), name='post-by-tag'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post-comment/', views.CommentView.as_view(), name='post-comment'),
    path("newsletter/",views.NewsletterView.as_view(),name="newsletter"),
    path("post-search/",views.PostSearchView.as_view(),name="post-search"),
    
]
