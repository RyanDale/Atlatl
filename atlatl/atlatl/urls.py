from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atlatl.views.home', name='home'),
    # url(r'^atlatl/', include('atlatl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^houses/', 'atlatltest.views.houses',name="Houses"),
    url(r'^admin/', include(admin.site.urls)),
)
