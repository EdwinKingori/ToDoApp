from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="tasks"),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('create_task/', views.CreateTask.as_view(), name="task_create"),
    path('update_task/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('delete_task/<int:pk>/', views.DeleteTasks.as_view(), name="task_delete")
]
