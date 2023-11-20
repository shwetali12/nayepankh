from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate,logout # Create your views here.
from django.contrib.auth.models import User
from .forms import Feedbackform
from .forms import PostForm
from .forms import CommentForm
from .models import Post,Comment
def index(request):
    return render(request,"index.html")


def certificates(request):
    return render(request,'certificates.html')

def about(request):
    return render(request,'about.html')

def news(request):
    return render(request,'news.html')

def donate(request):
    return render(request,'donate.html')

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your Password1  and password2 are not same.")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginpage')
    return render(request, 'signuppage.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1= request.POST.get('password1')
        print(username,password1)
        user=authenticate(request,username=username,password=password1)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            print(username,password1)
            return HttpResponse("Password is incorrect")
        
    return render(request,'loginpage.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

def feedback(request):
    if request.method == 'POST':
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = Feedbackform()
    return render(request,'feedback.html',{'form':form})

def thank_you(request):
    return render(request,'thank_you.html')


def community(request):
    posts = Post.objects.all()
    return render(request,'community.html',{'posts':posts})

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            new_post.author = request.user
            new_post.save()
            return redirect('post_detail', id=new_post.id)
    else:
        post_form = PostForm()

    return render(request, 'create_post.html', {'post_form': post_form})

def post_detail(request, id):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', id=id)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def comment(request, id):
    post = get_object_or_404(Post, pk=id)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post

            # Ensure that the author is set to the current user
            if request.user.is_authenticated:
                new_comment.author = request.user
                new_comment.save()
                return redirect('post_detail', id=id)
            else:
                # Handle the case when the user is not authenticated
                return redirect('login')  # Redirect to the login page or handle as appropriate
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comment_form': comment_form})