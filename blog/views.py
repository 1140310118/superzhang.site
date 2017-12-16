from django.shortcuts import render,loader
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseNotFound
from markdown import markdown
import os,re
import urllib.request

from blog.lib import checkMobile
from blog.models import BlogsPost

def home(request):
	return render_to_response('home.html',{})

# 供用户查看的文章列表
def blog(request):
	return render_to_response('blog.html',{})

# 用户查看某一篇博文
def blog_article(request,url):
	post=BlogsPost.objects.filter(url=url)[0]
	timestamp=post.timestamp
	# https://segmentfault.com/q/1010000004606334
	post.body=markdown(post.body,extensions=['tables'])
	header_fixed=post.addition_control_msg[0]
	font_style=post.addition_control_msg[1] # 0 是 微软雅黑，1 是华文宋体
	from_mobile=checkMobile(request)
	dic={'url':url,'timestamp':timestamp,'post':post,
			"header_fixed":header_fixed,
			"font_style":font_style,
			"from_mobile":from_mobile}
	return render_to_response('blog_article.html',dic)

def get_markdown(request,url):
	post=BlogsPost.objects.filter(url=url)[0]
	link="http://www.superzhang.site/blog/"+url
	link=''.join(('[',link,']','(',link,')'))
	str='##'+post.title+'\n\n'+post.body+'\n\n本文链接：'+link
	# print (str)
	response=HttpResponse(str)
	response['Content-Type'] = 'text/plain;charset=UTF8'
	return response

def print(request,url):
	## 为了方便打印输出。
	post=BlogsPost.objects.filter(url=url)[0]
	# https://segmentfault.com/q/1010000004606334
	post.body=markdown(post.body,extensions=['tables'])
	return render_to_response('child/print.html',{'post':post})

def latex_equation(request):
	url=request.get_full_path()
	url=urllib.request.unquote(url)
	_r=re.findall(r"\?[\s\S]*",url) #匹配包括换行符
	if _r:
		equation_before=_r[0][1:] #去除?
	else:
		equation_before=""
	equation_after=markdown("$$%s$$"%equation_before,extensions=['tables'])
	contexts={'equation_after':equation_after,'equation_before':equation_before}
	return render_to_response('child/latex.html',contexts)


def leave_message(request):
	return render_to_response('message.html',{})

def about(request):
	from_mobile=checkMobile(request)
	post=BlogsPost.objects.filter(url='about')[0]
	post.body=markdown(post.body,extensions=['tables'])
	dic={'post':post,'hide_bottom_small':"1","from_mobile":from_mobile}
	return render_to_response('blog_article.html',dic)

def links(request):
	from_mobile=checkMobile(request)
	post=BlogsPost.objects.filter(url='links')[0]
	post.body=markdown(post.body,extensions=['tables'])
	dic={'post':post,'hide_bottom_small':"1","from_mobile":from_mobile}
	return render_to_response('blog_article.html',dic)

def ufldl(request,url="welcome-to-the-deep-learning-tutorial"):
	from_mobile=checkMobile(request)
	all_list=BlogsPost.objects.all()
	blog_list=all_list.filter(tag='UFLDL',posted=True)
	post=all_list.filter(url=url)[0]
	post.body=markdown(post.body,extensions=['tables'])
	dic={"blog_list":blog_list,'post':post,'timestamp':post.timestamp,"from_mobile":from_mobile}
	return render_to_response('ufldl.html',dic)

###################################################################################33
# 以下方法生成的页面，仅供其他页面调用

# 网站顶部
def top(request):
	from_mobile=checkMobile(request)
	return render_to_response('child/top.html',{"from_mobile":from_mobile})

# 网站底部
def bottom(request):
	return render_to_response('child/bottom.html',{})

# 通用的文章样式
def article(request,url):
	post=BlogsPost.objects.filter(url=url)[0]
	# https://segmentfault.com/q/1010000004606334
	post.body=markdown(post.body,extensions=['tables'])
	return render_to_response('child/article.html',{'post':post})	

# 手机端的文章样式
def wap_article(request,url):
	post=BlogsPost.objects.filter(url=url)[0]
	# https://segmentfault.com/q/1010000004606334
	post.body=markdown(post.body,extensions=['tables'])
	return render_to_response('child/wap_article.html',{'post':post})	

# 博文列表
def blog_list(request,tag):
	_tags=BlogsPost.objects.values("tag").distinct()
	exclude_tag_list=['about','links','test','UFLDL']

	## get all
	all_list=BlogsPost.objects.filter(posted=True)
	for et in exclude_tag_list:
		all_list=all_list.exclude(tag=et)	
	num=len(all_list)
	tags=[('所有',num)]
	
	for t in _tags:
		# multi tag
		if ',' in t['tag']:
			continue
		if t['tag'] in exclude_tag_list:
			continue
		# http://blog.csdn.net/u013510614/article/details/50187515
		bl = all_list.filter(tag__contains=t['tag'])
		num = len(bl)
		if num!=0:
			tags.append((t['tag'],num))

	if tag!="所有":
		blog_list=all_list.filter(tag__contains=tag)
		num=len(blog_list)
		# tag=(tag,num)
	else:
		blog_list=all_list
		tag=tags[0]
# .........................
	blog_by_year={}
	for post in blog_list:
		post.date=post.timestamp.strftime('%Y/%m/%d')
		year=post.timestamp.year
		if year in blog_by_year:
			blog_by_year[year].append(post)
		else:
			blog_by_year[year]=[post]
	blog_by_year=sorted(blog_by_year.items(),reverse=True)
	for year_post in blog_by_year:
		year_post[1].sort(reverse=True,key=lambda i:i.timestamp)
	
	from_mobile=checkMobile(request)
	context={'tags':tags,'tag':tag,'blog_by_year':blog_by_year,"from_mobile":from_mobile}
	
	return render_to_response('child/blog_list.html',context)
