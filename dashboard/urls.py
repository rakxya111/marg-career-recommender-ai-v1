from django.urls import path
from dashboard import views

urlpatterns = [

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path("tag-list/",views.TagListView.as_view(),name="tag-list"),
    path("tag-delete/<int:pk>/",views.TagDeleteView.as_view(),name="tag-delete"),
    path("tag-update/<int:pk>",views.TagUpdateView.as_view(),name="tag-update"),
    path("tag-create/",views.TagCreateView.as_view(),name="tag-create"),


    path("post-list-view/",views.PostListView.as_view(),name="post-list-view"),
    path("post-create/",views.PostCreateView.as_view(),name="post-create"),
    path("post-delete/<int:pk>/",views.PostDeleteView.as_view(),name="post-delete"),
    path("post-update/<int:pk>/",views.PostUpdateView.as_view(),name="post-update"),
    path("dash-post-detail/<int:pk>/",views.PostDetailView.as_view(),name="dash-post-detail"),
    path("post-publish-view/<int:pk>",views.PostPublishView.as_view(),name="post-publish-view"),

    path("inactive-post-view/",views.InactivePostListView.as_view(),name="inactive-post-view"),
    path("make-active-view/<int:pk>/",views.MakeActiveView.as_view(),name="make-active-view"),
    path("de-active-view/<int:pk>/",views.DeActiveView.as_view(),name="de-active-view"),

]