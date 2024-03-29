"""
URL configuration for jetsonrobotwebcontroller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jetsonrobotwebcontroller.views import app, webcam_feed, webcam_deactivated, dummy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app),
    path('webcam', webcam_feed, name = 'webcam_feed'),
    path('streamer-cat', webcam_deactivated, name = 'webcam_deactivated'),
    #path('webcam_feed_inicial', webcam_feed_inicial, name = 'webcam_feed_inicial'),
    path('dummy', dummy, name = 'dummy'),
]
