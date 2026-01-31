from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'), # NEW!
    ]
