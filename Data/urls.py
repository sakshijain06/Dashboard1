from django.conf.urls import patterns, include, url
from Data import script


urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^uploadData/', script.fetchTestCaseInfoAndPersist)
)
