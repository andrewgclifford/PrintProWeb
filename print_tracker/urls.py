from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jobs.views import JobViewSet

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] 