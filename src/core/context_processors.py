from django.db.models import Count
from .models import *


def post_processor(request):
    """
    定义上下文处理器
    全局共享数据
    """
    return {
        "BIO": Profile.objects.first().bio,
        "CATEGORIES": Category.objects.values('id', 'name').annotate(Count('posts')),
        "LATEST_POSTS": Post.published.all()[:5],
        "CHOSE_POSTS": Post.published.filter(flag=True).all()[:5],
    }