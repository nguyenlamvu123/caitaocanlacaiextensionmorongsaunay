from django.urls import path

from . import views

app_name = "django_import_export"

urlpatterns = [
    path('', views.index, name='index'),
]
