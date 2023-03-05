
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accaunts/', include('django.contrib.auth.urls')),
    path('accaunts/',include('accaunts.urls')),
    path('',include('homepage.urls')),
]
