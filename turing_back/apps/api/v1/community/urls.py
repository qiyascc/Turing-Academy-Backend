from django.urls import path
from .views import CommunityListView, CommunityDetailView, AdvantageListView

urlpatterns = [
    path('', CommunityListView.as_view(), name='community-list'),
    path('advantages/', AdvantageListView.as_view(), name='advantage-list'),
]