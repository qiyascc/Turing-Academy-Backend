from rest_framework import generics
from .models import Community, Advantage
from .serializers import CommunitySerializer, AdvantageSerializer

class CommunityListView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class CommunityDetailView(generics.RetrieveAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class AdvantageListView(generics.ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer