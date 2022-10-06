from django.conf.urls import url
from .views import (
    Post_idd,
)

urlpatterns[
    url(r'^Post_id/(?P<pk>\d+)/$', Post_idd, name='Post_idd')
]