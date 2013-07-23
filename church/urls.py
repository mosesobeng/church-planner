from django.conf.urls import patterns, include, url
from django.conf import settings
from piston.resource import Resource
from planner.handlers import CalcHandler
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

calc_resource = CsrfExemptResource( CalcHandler )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Church.views.home', name='home'),
    # url(r'^Church/', include('Church.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^planner$', 'planner.views.home',name="home"),
    url(r'^member-login$','planner.views.login', name='login'),
    url(r'^member-logout$','planner.views.logout', name='logout'),
    url(r'^church-planner-api/(?P<expression>.*)$', calc_resource),
    url(r'^static/bootstrap','django.views.static.serve', name='bootstrap'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
