from django.urls import path
from .views import EventListView, EventDetailView, last_events, restricted_view

urlpatterns = [
    path('all/', EventListView.as_view(), name='event-list'),
    path('all/last/', last_events, name='last-events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('', restricted_view),
]
