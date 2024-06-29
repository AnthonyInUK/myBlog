from django.contrib import admin
from django import forms
from .models import Profile, Category, Post, Comment, Slide

from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Register your models here.


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'link', 'order')
    link_fields = ('title',)
    list_editable = ('order',)
    ordering = ('-order', 'id')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'title', 'phone', 'created')
    ordering = ('-created',)

admin.site.register(Profile, ProfileAdmin)


class CategoryAdminForm(forms.ModelForm):
    """类别管理表单"""
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "description": forms.Textarea
        }


# 注册类别管理
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """类别后台管理"""
    form = CategoryAdminForm
    list_display = ('slug', 'name', 'order')
    list_editable = ('order', )


class PostAdminForm(forms.ModelForm):
    """日志管理表单"""
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'summary': forms.Textarea,
            'body': SummernoteWidget(),
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """日志后台管理"""
    form = PostAdminForm
    list_per_page = 20
    list_display = ('title', 'slug', 'category', 'views', 'flag', 'status')
    search_fields = ('title', 'body')
    list_filter = ('category', 'flag', 'status')
    date_hierarchy = 'created'
    ordering = ('-created', 'status')


# 注册日志评论管理
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('post', 'name', 'ip', 'active', 'created')
    list_filter = ('active', 'created')
    ordering = ('-created', )