from django.shortcuts import render

# Create your views here.
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