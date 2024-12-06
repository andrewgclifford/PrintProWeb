from django.urls import path
from . import template_views

urlpatterns = [
    path('', template_views.job_list, name='jobs'),
    path('create/', template_views.job_create, name='job_create'),
    path('<int:pk>/', template_views.job_detail, name='job_detail'),
    path('<int:pk>/update/', template_views.job_update, name='job_update'),
]
