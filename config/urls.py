from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faculties/',include('faculties.urls')),
    path('api/communication/',include('communication.urls')),
    path('api/admission/',include('admissions.urls')),
]
