from django.urls import path
from recursos.views import MaterialViewSet

urlpatterns = [
    path('materiales/', MaterialViewSet.as_view(), name="material-all")
]