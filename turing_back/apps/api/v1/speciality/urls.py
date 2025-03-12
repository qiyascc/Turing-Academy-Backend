from django.urls import path
from .views import SpecialityListView, SpecialityDetailView, last_specialities, restricted_view

urlpatterns = [
    path('all/', SpecialityListView.as_view(), name='speciality-list'),
    path('<int:pk>/', SpecialityDetailView.as_view(), name='speciality-detail'),
    path('last/', last_specialities, name='last-specialities'),
    path('', restricted_view),

]