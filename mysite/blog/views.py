from django.shortcuts import render
from django.views import View
from .models import Post

class PostListView(View):
    def get(self, request):
        # Query all posts from database
        all_posts = Post.objects.all()
        
        # Create context dictionary
        context = {
            'all_posts': all_posts
        }
        
        # Render template with context
        return render(request, 'post_list.html', context)