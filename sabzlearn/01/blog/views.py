from django.shortcuts import render
from django.http import HttpResponse,  Http404
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return HttpResponse("index")
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts , 2)
    page_number = request.GET.get('page' , 1)
    posts = paginator.page(page_number)
    context = {
        'posts' : posts,
    }
    return render(request,"blog/list.html", context)

def post_detail(request , id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404("No post found")
    context = {
        'post': post,
    }
    return render(request, "blog/detail.html", context)