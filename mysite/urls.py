from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #=================admin======================
    url(r'^admin/', include(admin.site.urls)),
    #=================home=======================
    url(r'^$','blog.views.home'),
    url(r'^dir/$','blog.views.dir'),
    url(r'^home/$','blog.views.home'),
    #=================blog=======================
    # 被调用的页面
    url(r'^top/$','blog.views.top'),
    url(r'^bottom/$','blog.views.bottom'),
    url(r'^blog_list/(?P<tag>.*)/$','blog.views.blog_list'),
    url(r'^article/(?P<url>.*)/$','blog.views.article'),
    url(r'^wap_article/(?P<url>.*)/$','blog.views.wap_article'),
    # 用户所看到的页面
    url(r'^blog/$','blog.views.blog'),
    url(r'^blog/(?P<url>.*)/$','blog.views.blog_article'),
    url(r'^ufldl/(?P<url>.*)/$','blog.views.ufldl'),
    url(r'^ufldl/$','blog.views.ufldl'),
    url(r'^message','blog.views.leave_message'),
    url(r'^about','blog.views.about'),
    url(r'^links','blog.views.links'),
    # 工具页面
    url(r'^markdown/(?P<url>.*).md$','blog.views.get_markdown'),
    url(r'^print/(?P<url>.*)/$','blog.views.print'),


    #=================latex=======================
    url(r'^latex$','latex.views.latex_equation'),
    #=================pnm========================
    url(r'^pnm$','pnm.views.home'),
    url(r'^pnm/(?P<paper_id>.*)/$','pnm.views.view'),
    url(r'^_add_note/$','pnm.views.add_note'),
    url(r'^_modify_note/$','pnm.views.modify_note'),
    url(r'^_delete_note/$','pnm.views.delete_note'),
]
