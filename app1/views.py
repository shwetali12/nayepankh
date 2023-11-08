from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout # Create your views here.
from django.contrib.auth.models import User
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

