from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import Profile, Category, Post, Comment, Slide
from .forms import CommentForm

from taggit.models import Tag


# Create your views here.


def index(request):
    # items = Post.objects.filter(status='published')[:10]
    items = Post.published.all()[:10]
    slides = Slide.objects.all()
    return render(request, "index.html", {
        "items": items,
        "slides": slides,
    })


def posts(request):
    items = Post.published.all()

    # 按标签、分类 过滤
    tag = request.GET.get('tag', None)
    cat = request.GET.get('cat', None)  # 1 2 3

    if tag:
        tag_obj = Tag.objects.get(slug=tag)
        items = items.filter(tags__in=[tag_obj])     # tag_obj in tags

    if cat:
        items = items.filter(category__id=cat)       # category.id = 3

    paginator = Paginator(items, 10)        # 分页器
    page = request.GET.get('page')          # 地址栏获取查询字符串页码

    try:
        items = paginator.page(page)        # 获取当前页数据集合
    except PageNotAnInteger:
        items = paginator.page(1)           # 默认显示第 1 页
    except EmptyPage:
        items = paginator.page(paginator.num_pages) # 空页面显示最后一页

    # categories = Category.objects.all()
    return render(request, "post-list.html", {
        "items": items,
        # "categories": categories,
    })


def details(request, slug):
    item = Post.objects.get(slug=slug)
    # tags = item.tags.split(",")
    
    form = CommentForm()

    try:
        prev_post = item.get_next_by_created()
    except Post.DoesNotExist:
        prev_post = None

    try:
        next_post = item.get_previous_by_created()
    except Post.DoesNotExist:
        next_post = None

    if request.method == 'POST':
        # 手动获取表单数据
        # name = request.POST.get('name', None)
        # body = request.POST.get('body', None)
        # if name and body:
        #     comment = Comment()
        #     comment.post = item
        #     comment.name = name
        #     comment.body = body
        #     comment.ip = get_client_ip(request)
        #     comment.save()

        # 从 CommentForm 实例获取数据
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = item
            comment.ip = get_client_ip(request)
            comment.save()

        return redirect(item)

    return render(request, 'details.html', 
    {
        'item': item, 
        # 'tags': tags, 
        'form': form,
        'prev_post': prev_post, 
        'next_post': next_post})


def search_posts(request):
    items = Post.published.all()

    q = request.GET.get('q', None)
    if q.strip():
        items = items.filter(title__contains=q)
    else:
        return redirect(reverse('posts'))

    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "post-search.html",
    {"page": page, "items":posts})


def get_client_ip(request):
    """获取客户端IP"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def about(request):
    item = Profile.objects.get(id=1)
    item.hits += 1
    item.save()
    return render(request, 'about.html', {"item": item})
