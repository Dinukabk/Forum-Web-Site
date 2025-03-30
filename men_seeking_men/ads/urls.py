from django.urls import path
from .views import AdListCreateAPIView, AdDetailAPIView

urlpatterns = [
    path('ads/', AdListCreateAPIView.as_view(), name='ad-list-create'),
    path('ads/<int:pk>/', AdDetailAPIView.as_view(), name='ad-detail'),
]
