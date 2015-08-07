from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'TheftControlSystem.views.home', name='home'),
    url(r'^(?i)victim/', include('TheftControlSystem.apps.VictimMap.urls')),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
