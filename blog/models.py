from django.db import models
from django.contrib import admin


class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    tag = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=150,default="11")
    posted = models.BooleanField(default=True)
    category = models.CharField(max_length=150,default="null")
    # 0 控制标题栏是否滑动　默认0，表示滑动
    # 1 控制字体风格       默认1，表示华文宋体；0表示微软雅黑
    #23 控制博文顺序，一般在教程类博文中使用
    addition_control_msg=models.CharField(max_length=150,default="0100000000")


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','tag','posted','timestamp')
    # https://code.ziqiangxuetang.com/django/django-admin.html
    search_fields= ('tag',)


admin.site.register(BlogsPost,BlogPostAdmin)