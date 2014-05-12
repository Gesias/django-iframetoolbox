from django.conf.urls import patterns, url


urlpatterns = patterns(
    'iframetoolbox.views',
    url(r'iframefix/$', 'iframe_fix'),
)
