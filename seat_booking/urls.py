from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),  # Display all seats
    path('book_slot/<int:slot_id>/', views.BookSlotView.as_view(), name='book_slot'),  # Form for booking slot
]
