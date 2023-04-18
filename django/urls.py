from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    re_path(r'^detail/(?P<item_id>\d+)/$', views.detail, name='detail'),
    path('data_model/', views.data_model, name='data_model'),
]
