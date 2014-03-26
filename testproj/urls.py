from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'testproj.views.home', name='home'),
    url(r'^linkedintest2/$', 'testproj.views.linkedintest2', name='linkedintest2'),
    url(r'^resultsontheway/$', 'testproj.views.resultsontheway', name='resultsontheway'),
    #(r'^accounts/', include('allauth.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
