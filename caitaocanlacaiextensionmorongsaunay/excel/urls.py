##from django.urls import path
##
##from . import views
##
##app_name = "myapp"
##
##urlpatterns = [
##    path('', views.index, name='index'),
##]
from django.urls import path

from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]
