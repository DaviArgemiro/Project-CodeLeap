from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from postSite.models import Post

# Create your views here.
def post_view(request):
    return render(request, 'Login/loginPage.html')

def post_login(request):
    user = request.POST.get('user')

    return redirect('post_list', user=user)

def post_list(request, user):
    posts = Post.objects.all().order_by('username')
    user = user

    return render(request, 'PostPage/postPage.html', {'posts': posts, 'user': user})
    
def new_post_view(request):
    user = request.POST.get('user')
    new_post = Post()
    new_post.username = user
    new_post.title = request.POST.get('title')
    new_post.content = request.POST.get('content')

    new_post.save()

    return redirect('post_list', user=user)

def confirm_delete(request, pk):

    post = Post.objects.get(pk=pk)

    return render(request, 'DeleteOrEditPage/deletePage.html', {'post': post})

def delete_post(request, pk):
    
    post = Post.objects.get(pk=pk)
    user = post.username
    post.delete()

    return redirect('post_list', user=user)

def confirm_edit(request, pk):

    post = Post.objects.get(pk=pk)

    return render(request, 'DeleteOrEditPage/editPage.html', {'post': post})

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)

    post.title = request.POST.get('title')
    post.content = request.POST.get('content')

    post.save()

    return redirect('post_list', user=post.username)
