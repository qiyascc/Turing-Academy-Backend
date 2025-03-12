from rest_framework import generics
from .models import General
from .serializers import GeneralSerializer

class GeneralListView(generics.ListAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer

class GeneralDetailView(generics.RetrieveAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer