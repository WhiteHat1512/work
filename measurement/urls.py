from django.urls import path

from measurement.views import create_sensor, update_sensor, add_measurement, sensor_detail, sensor_list

urlpatterns = [
    path('sensor/', create_sensor.as_view()),
    path('sensor/<pk>', update_sensor.as_view()),
    path('add/', add_measurement.as_view()),
    path('sensor_detail/<pk>', sensor_detail.as_view()),
    path('sensor_list/', sensor_list.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]