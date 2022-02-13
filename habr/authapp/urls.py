from django.urls import path, include
from .views import UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, logout, login

app_name = 'auth'

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('reg/', UserCreateView.as_view(), name='users_create'),
    path('edit/', UserUpdateView.as_view(), name='users_update'),
    path('remove/', UserDeleteView.as_view(), name='users_remove'),
    #URLs for activation accounts
]
