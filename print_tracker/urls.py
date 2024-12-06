from django.contrib import admin
from django.urls import path, include
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