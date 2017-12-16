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
    #０　控制标题栏是否滑动　默认是
    addition_control_msg=models.CharField(max_length=150,default="0100000000")


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)