from django.urls import path
from .views import PartnerListView, PartnerDetailView

urlpatterns = [
    path('all/', PartnerListView.as_view(), name='partner-list'),
    path('<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
]