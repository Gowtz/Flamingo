from typing import ContextManager
from django.shortcuts import render
from blog.models import BlogModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    posts = BlogModel.objects.all().order_by('-id')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)
    content = {'posts':posts_list,
                'page':page}
    return render(request, 'index.html', content)
