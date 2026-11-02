from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_flight, name='add_flight'),
    path('update/<int:id>/', views.update_flight, name='update_flight'),
    path('delete/<int:id>/', views.delete_flight, name='delete_flight'),
    path('book/', views.book_flight, name='book_flight'),
]


