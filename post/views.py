# views.py
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import PostImage


def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assuming you want to associate the post with the logged-in user
            post.save()

            for image in images:
                PostImage.objects.create(post=post, image=image)

            return redirect('home')  # Redirect to home or any other page

    else:
        form = PostForm()

    return render(request, 'post/addpost.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    user = request.user

    # Check if the user already liked the post
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    # Return a JSON response
    return JsonResponse({"liked": liked, "total_likes": post.likes.count()})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

@login_required(login_url='login')
def comment_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(post=post, user=request.user, comment=comment_text)
        return redirect('home')  # Redirect to the home page after submission
    
    comments = Comment.objects.filter(post=post).order_by('-date')
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'post/comment_page.html', context)


@login_required(login_url='login')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect('home')
