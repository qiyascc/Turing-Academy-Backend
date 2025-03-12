from django.urls import path, include

urlpatterns = [
    path('event/', include('turing_back.apps.api.v1.event.urls')),
    path('partner/', include('turing_back.apps.api.v1.partner.urls')),
    path('general/', include('turing_back.apps.api.v1.general.urls')),
    path('graduate/', include('turing_back.apps.api.v1.graduate.urls')),
    path('community/', include('turing_back.apps.api.v1.community.urls')),
    path('test/', include('turing_back.apps.api.v1.test_and_contact.urls.url-test')),
    path('contact/', include('turing_back.apps.api.v1.test_and_contact.urls.url-contact')),
    path('speciality/', include('turing_back.apps.api.v1.speciality.urls')),
    path('schoolarship/', include('turing_back.apps.api.v1.schoolarship.urls')),

]