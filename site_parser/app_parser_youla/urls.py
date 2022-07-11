
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('path_start_parser/', views.start, name='name_path_start_parser'),
    path('path_FindLinks/', views.real_time_display, name='name_path_FindLinks'),
    path('path_get_proxies_and_links_category/', views.get_proxies_and_links_category, name='name_path_get_proxies_and_links_category'),
    path('path_read_links_category_and_proxies_txt/', views.read_links_category_and_proxies_txt, name='name_read_links_category_and_proxies_txt'),
    path('path_stop_parser/', views.stop_parser, name='name_stop_parser'),

]
