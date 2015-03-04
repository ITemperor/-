from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'myblog.views.home'),
    url(r'^hello$', 'myblog.views.hello'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
