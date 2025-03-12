from django.urls import path
from .views import GeneralListView, GeneralDetailView

urlpatterns = [
    path('', GeneralListView.as_view(), name='general-list'),
    path('<int:pk>/', GeneralDetailView.as_view(), name='general-detail'),
]