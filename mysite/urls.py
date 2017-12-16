from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.home'),
    url(r'^home/$','blog.views.home'),
    url(r'^top/$','blog.views.top'),
    url(r'^bottom/$','blog.views.bottom'),
    url(r'^blog/$','blog.views.blog'),
    # ex /blog_list/latex
    url(r'^blog_list/(?P<tag>.*)/$','blog.views.blog_list'),
    url(r'^blog/(?P<url>.*)/$','blog.views.blog_article'),
    url(r'^article/(?P<url>.*)/$','blog.views.article'),
    url(r'^wap_article/(?P<url>.*)/$','blog.views.wap_article'),
    url(r'^markdown/(?P<url>.*).md$','blog.views.get_markdown'),
    url(r'^print/(?P<url>.*)/$','blog.views.print'),
    url(r'^latex$','blog.views.latex_equation'),
    url(r'^message','blog.views.leave_message'),
    url(r'^about','blog.views.about'),
    url(r'^links','blog.views.links'),
    url(r'^ufldl/(?P<url>.*)/$','blog.views.ufldl'),
    url(r'^ufldl/$','blog.views.ufldl'),
    # url(r'^ufldl/(?P<url>.*)','blog.views.ufldl'),
]
