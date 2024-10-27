#1-url maapping in local file
from django.urls import path
#2-importing views
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<int:pk>', views.Post, name='post'),
]
