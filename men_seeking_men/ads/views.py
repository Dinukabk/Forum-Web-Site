from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer

# List all approved ads and allow creation of a new ad.
class AdListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ad.objects.filter(approved=True).order_by('-posted_at')
    serializer_class = AdSerializer

# Retrieve the details of a specific ad.
class AdDetailAPIView(generics.RetrieveAPIView):
    queryset = Ad.objects.filter(approved=True)
    serializer_class = AdSerializer
