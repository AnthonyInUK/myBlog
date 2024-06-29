from django import forms
from django.core import validators

from .models import Comment


# class CommentForm(forms.Form):
#     """手动声明表单类"""
#     name = forms.CharField(max_length=50, label='姓名', validators=[validators.MinLengthValidator(3, '姓名长度不得少于3个字符！')])
#     body = forms.CharField(label='正文')
    

class CommentForm(forms.ModelForm):
    """根据数据模型生成表单"""
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            "name": forms.TextInput(attrs = {
                'class': 'border rounded-md p-2 text-sm',
                'placeholder': '姓名',
            }),
            "body": forms.Textarea(attrs={
                'class': 'w-full border rounded-md p-2 text-sm',
                'rows': 3,
                'placeholder': '留下您的评论...'
            }),
        }
