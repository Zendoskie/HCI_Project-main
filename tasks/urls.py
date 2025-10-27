from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Function-based view - root URL
    path('', views.task_list, name='task_list'),
    
    # Class-based view - /cbv/ URL
    path('cbv/', views.TaskListView.as_view(), name='task_list_cbv'),
    
    # Task actions
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:pk>/', views.TaskUpdateView.as_view(), name='edit_task'),
    path('delete-cbv/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task_cbv'),
    
    # Statistics
    path('stats/', views.stats_page, name='stats_page'),
    path('api/stats/', views.task_stats_api, name='task_stats_api'),
]
