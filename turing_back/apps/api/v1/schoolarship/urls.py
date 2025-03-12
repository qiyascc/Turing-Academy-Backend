from django.urls import path
from .views import SchoolarshipListView, SchoolarshipDetailView

urlpatterns = [
    path('all/', SchoolarshipListView.as_view(), name='schoolarship-list'),
    path('<int:pk>/', SchoolarshipDetailView.as_view(), name='schoolarship-detail'),
]