from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from .forms import PostForm

class PostListView(View):
    def get(self, request):
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}
        return render(request, 'post_list.html', context)


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'post_create.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        context = {'form': form}
        return render(request, 'post_create.html', context)


# NEW: DETAIL VIEW
class PostDetailView(View):
    def get(self, request, pk):
        # Get the specific post by ID (pk = primary key)
        # If post doesn't exist, show 404 error
        post = get_object_or_404(Post, pk=pk)
        
        context = {'post': post}
        return render(request, 'post_detail.html', context)