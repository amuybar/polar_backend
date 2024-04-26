# monitoring_app/urls.py
from django.urls import path
from .views import add_health_data, update_health_data, delete_health_data, get_health_data

app_name = 'monitoring_app'

urlpatterns = [
    path('add/', add_health_data, name='add'),
    path('<int:data_id>/update/', update_health_data, name='update'),
    path('<int:data_id>/delete/', delete_health_data, name='delete'),
    path('get/', get_health_data, name='get'),
]
