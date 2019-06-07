from django.urls import path
from .views import ListCreateCategoriasView, ListCreateSongsView, ListCreateMaterialView, ListCreateRequest, ListUser
from .views import SongsDetailView, MaterialDetailView, CategoriasDetailView, RequestDetailView, UserDetailView ,LoginView, RegisterUsers

urlpatterns = [
    path('users/', ListUser.as_view(), name="users-list"),
    path('users/<str:username>/', UserDetailView.as_view(), name="users-detail"),
    path('categorias/', ListCreateCategoriasView.as_view(), name="categorias-list-create"),
    path('categorias/<int:pk>/', CategoriasDetailView.as_view(), name="categorias-detail"),
    path('material/', ListCreateMaterialView.as_view(), name="material-list-create"),
    path('material/<int:pk>/', MaterialDetailView.as_view(), name="material-detail"),
    path('request/', ListCreateRequest.as_view(), name="request-list-create"),
    path('request/<int:pk>/', RequestDetailView.as_view(), name="request-detail"),
    path('songs/', ListCreateSongsView.as_view(), name="songs-list-create"),
    path('songs/<int:pk>/', SongsDetailView.as_view(), name="songs-detail"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register")
]
