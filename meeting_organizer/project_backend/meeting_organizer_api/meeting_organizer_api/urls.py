"""meeting_organizer_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403, handler400

from api.api import project_api
from api.views import redirect_homepage_to_api

handler404 = 'api.views.view_404'
handler500 = 'api.views.view_500'

urlpatterns = [
    path('admin/', admin.site.urls), ## django admin panel url to modify the database 
    path('', redirect_homepage_to_api), ## a custom route that redirects homapage to api page
    path("api-v1/", project_api.urls), ## api url
]
