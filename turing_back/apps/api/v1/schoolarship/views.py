from rest_framework import generics
from .models import Schoolarship
from .serializers import SchoolarshipSerializer

class SchoolarshipListView(generics.ListAPIView):
    queryset = Schoolarship.objects.all()
    serializer_class = SchoolarshipSerializer

class SchoolarshipDetailView(generics.RetrieveAPIView):
    queryset = Schoolarship.objects.all()
    serializer_class = SchoolarshipSerializer