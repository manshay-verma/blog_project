from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author':'ms.py',
        'title':'blog post 1',
        'content':'first post',
        'date':'may 10,2025',
    },
    {
        'author':'my.py',
        'title':'blog post 2',
        'content':'second post',
        'date':'May 11,2025',
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})