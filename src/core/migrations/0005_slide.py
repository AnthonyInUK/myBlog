# Generated by Django 4.0.4 on 2022-07-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='标题')),
                ('sub_title', models.CharField(blank=True, max_length=120, verbose_name='副标题')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('link', models.URLField(blank=True, max_length=120, verbose_name='链接')),
                ('img', models.ImageField(blank=True, upload_to='uploads', verbose_name='图片')),
                ('order', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '首页轮播图',
                'verbose_name_plural': '首页轮播图',
                'ordering': ('-order', 'id'),
            },
        ),
    ]