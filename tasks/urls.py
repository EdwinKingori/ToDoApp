from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name="register"),
    path("", views.StartingPage.as_view(), name="tasks"),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('create_task/', views.CreateTask.as_view(), name="task_create"),
    path('update_task/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('delete_task/<int:pk>/', views.DeleteTasks.as_view(), name="task_delete")
]
