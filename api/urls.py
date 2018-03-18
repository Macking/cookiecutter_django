from django.conf.urls import url

from . import views

app_name = 'api'
urlpatterns = [
    url(r'^v1/echo/$', views.api_echo),
]
