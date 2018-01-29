from django.shortcuts import render
from .models import post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post1 = get_object_or_404(post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post1})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post1 = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post2 = form.save(commit=False)
            post2.author = request.user
            post2.published_date = timezone.now()
            post2.save()
            return redirect('post_detail', pk=post2.pk)
    else:
        form = PostForm(instance=post1)
    return render(request, 'blog/post_edit.html', {'form': form})
