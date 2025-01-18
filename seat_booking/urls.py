from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),  # URL pattern for the home page that displays all seats
    path('book_slot/<int:slot_id>/', views.BookSlotView.as_view(), name='book_slot'),  # URL pattern for booking a slot with a specific slot ID
]
