from django.contrib import admin
from django.urls import include, path, re_path
from pybo.views import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]