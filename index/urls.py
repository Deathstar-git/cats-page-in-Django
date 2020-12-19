from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete/<str:name>/', views.delete, name='delete')
]
