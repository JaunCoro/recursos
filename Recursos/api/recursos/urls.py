from django.urls import path
from django.conf.urls import url
from recursos.views import MaterialViewSet

urlpatterns = [
    url(r'^materiales/$', MaterialViewSet.as_view(), name="recursos")
]