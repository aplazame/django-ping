from django.urls import re_path

from ping.views import status


urlpatterns = [
    url(r'^$', status, name='status'),
]
