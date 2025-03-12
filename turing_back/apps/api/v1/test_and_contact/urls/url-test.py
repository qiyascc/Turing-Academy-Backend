from django.urls import path
from ..views import TestListView, TestDetailView

urlpatterns = [
    path('all/', TestListView.as_view(), name='test-list'),
    path('<int:pk>/', TestDetailView.as_view(), name='test-detail'),
]