from django.urls import path
from todo import views
urlpatterns=[
    path('',views.TodoAPIView.as_view(),name='todos'),
    path('<int:id>',views.TodoDetailAPIView.as_view(),name='todo')
    
]