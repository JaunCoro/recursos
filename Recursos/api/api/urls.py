from django.conf import settings
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('recursos.urls', 'recursos'), namespace='recursos'))
]

urlpatterns += [
    path('api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
]