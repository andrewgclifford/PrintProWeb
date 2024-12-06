from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from jobs.views import JobViewSet
from .views import index, dashboard

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('jobs/', include('jobs.urls')),
]

# Add media files serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# Add static files serving in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)