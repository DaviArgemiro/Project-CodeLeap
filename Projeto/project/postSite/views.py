from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from postSite.models import Post

def post_view(request):
    posts = Post.objects.all()

    return render(request, 'PostPage/postPage.html', {'posts': posts})

def new_post_view(request):
    
    new_post = Post()

    new_post.username = request.POST['username']
    new_post.title = request.POST['title']
    new_post.content = request.POST['content']

    new_post.save()

    return redirect('post_list')

def delete_post_view(request, pk):

    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect('post_list')

    return render(request, 'DeleteOrEditPage/deletePage.html', {'post': post})

def edit_post_view(request, pk):

    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        post.username = request.POST['username']
        post.title = request.POST['title']
        post.content = request.POST['content']

        post.save()

        return redirect('post_list')

    return render(request, 'DeleteOrEditPage/editPage.html', {'post': post})