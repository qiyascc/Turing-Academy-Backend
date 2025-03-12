from rest_framework import generics
from .models import Test, Contact
from .serializers import TestSerializer, ContactSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetailView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class ContactCreateView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer