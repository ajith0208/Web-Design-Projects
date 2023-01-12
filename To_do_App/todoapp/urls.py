from django.urls import path

from todoapp import views
app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>', views.delete, name='delete'),
    path('update/<int:taskid>', views.update, name='update'),
    path('cbvhome', views.TaskLV.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDV.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUV.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeV.as_view(), name='cbvdelete'),
]

