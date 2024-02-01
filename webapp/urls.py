from django.urls import path 
from . import views 

urlpatterns = [
    path ('', views.home_page, name="homepage"), 
    path ('about/', views.about_page, name="aboutpage"),
    path ('reservation/', views.reservation_page, name="reservation"),
    path ('menu/', views.menu_page, name="menu"),
    path ('update_reservation/<int:pk>/', views.updateReservation, name="updateReservation"),
    path ('delete_reservation/<int:pk>/', views.deleteReservation, name="deleteReservation")
]