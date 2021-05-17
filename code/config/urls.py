from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('car_rent/', include('car_rent.urls')),
    path('cars/', include('car.urls')),
    path('customers/', include('customer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
