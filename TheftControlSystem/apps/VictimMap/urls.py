from django.conf.urls import include, url

from .views import convert_location_to_coordinates

urlpatterns = [
    # Examples:
    url(r'^(?i)convert/$',
        convert_location_to_coordinates, name='convert'),
    # url(r'^blog/', include('blog.urls')),

]
