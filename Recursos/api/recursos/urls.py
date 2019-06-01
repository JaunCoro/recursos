from django.urls import path
from django.conf.urls import url
from recursos.views import MaterialViewSet

urlpatterns = [
    path('materiales/', MaterialViewSet.as_view(), name="material-list-create")
]