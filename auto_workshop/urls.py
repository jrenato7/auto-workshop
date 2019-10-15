"""auto_workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from auto_workshop.core.views import home


urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
]


admin.site.site_header = "Sistema de Administração de Oficinas"
admin.site.site_title = "Sistema de Administração de Oficinas"
admin.site.index_title = "Sistema de Administração de Oficinas"
