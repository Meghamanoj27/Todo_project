from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('detail/<int:task_id>/', views.detail, name='detail'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    path('classbasedviewIndex/', views.TaskListView.as_view(), name='classbasedviewIndex'),
    path('cbvdetailview/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetailview'),
    path('cbvUpdateView/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvUpdateView'),
    path('cbvDeleteView/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvDeleteView'),
]
