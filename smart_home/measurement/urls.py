from django.urls import path

from measurement.views import SensorListCreateView, SensorRetrieveUpdateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-retrieve-update'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('sensors/<int:pk>/details/', SensorDetailView.as_view(), name='sensor-detail'),

    # TODO: зарегистрируйте необходимые маршруты
]
