from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('KMZERO.urls', 'KMZERO'), namespace='KMZERO')),
]