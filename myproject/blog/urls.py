from django.urls import path
from .views import home, register, login_view, logout_view, post_list, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    path('', home, name='home'),  # Маршрут для домашней страницы
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('posts/', post_list, name='post_list'),  # Измените на /posts/ для лучшей структуры
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/edit/<int:id>/', post_edit, name='post_edit'),
    path('post/delete/<int:id>/', post_delete, name='post_delete'),
]
