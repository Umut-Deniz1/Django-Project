from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.create, name="create" ),
    path('update/<str:pk>', views.update, name="update" ),
    path('delete/<str:pk>', views.delete, name="delete" ),
    path('', views.showUser, name="showUser" ),
]