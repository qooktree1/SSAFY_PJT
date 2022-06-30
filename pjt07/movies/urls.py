from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments_create/', views.comments_create, name='comments_create'),
    path('<int:pk>/<int:comment_pk>/comments_delete/', views.comments_delete, name='comments_delete'),
]


