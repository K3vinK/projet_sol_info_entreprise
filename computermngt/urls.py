from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('computerApp/', include('computerApp.urls')),
    path('admin/', admin.site.urls),
]