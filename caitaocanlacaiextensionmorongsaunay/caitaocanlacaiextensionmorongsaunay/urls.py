"""caitaocanlacaiextensionmorongsaunay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
##from django.contrib import admin
##from django.conf.urls import url, include
##from django.urls import path
##from django.conf import settings
##from django.conf.urls.static import static
##from django.shortcuts import render
##
##from chart import views as charrrrrrrrt
##
##def linhnhixinhdep(request): 
##    return render(request, 'danhvantienganh.html')
##
##urlpatterns = [
##    path('admin/', admin.site.urls),
##    path('charrt/', charrrrrrrrt.myFirstChart),
##    path('danhvantienganh/', linhnhixinhdep),
##]


###from movie_web_app import views as linhnhixinhdep
##
##urlpatterns = [
##    path('admin/', admin.site.urls),    
##    #path('linhnhixinhdep/', linhnhixinhdep.showvideo),
##    #path('movies/', include('movies.urls')),
##    path('3sic5Uploads/', include('BasicFileUploads.urls')),
##]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
####urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
####urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('excel.urls')),
]
