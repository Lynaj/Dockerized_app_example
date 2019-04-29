from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf.urls import include, url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from config.api import api

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
]
