from django.urls import path

from . import views


urlpatterns = [
    path('', views.port, name='port'),
    path('send_message', views.send_message, name="send_message"),
   
]