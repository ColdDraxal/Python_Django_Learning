"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from playground.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name="Landings"),
    path('about-us/', About, name="Abouts pages"),
    path('service/', Service, name="Services pages"),
    path('contact/', contact, name="contact"),
    path('student/<int:id>/', StudentbyId, name="studentById"),
    path('search/<str:name>/', SearchParam, name="search"),
    path('product/<slug:item>', productdetail, name="product"),
    path('file/<path:file_path>', Files, name="files"),
    path('home/', Index , name ="index page"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)