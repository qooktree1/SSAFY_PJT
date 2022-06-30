from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),  # update는 왜 PK값이 없을까요?
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),
]
