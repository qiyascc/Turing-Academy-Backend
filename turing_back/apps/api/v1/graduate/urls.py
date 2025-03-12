from django.urls import path
from .views import GraduateListView, GraduateDetailView, last_graduates, restricted_view

urlpatterns = [
    path('all/', GraduateListView.as_view(), name='graduate-list'),
    path('<int:pk>/', GraduateDetailView.as_view(), name='graduate-detail'),
    path('last/', last_graduates, name='last-graduates'),
    path('', restricted_view),

]