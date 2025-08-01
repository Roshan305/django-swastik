from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('register/', views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('', views.task_list, name='task-list'),
    path('tasks/<int:pk>/update/', views.task_update, name='task-update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task-delete'),

]