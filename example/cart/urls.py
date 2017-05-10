from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/(?P<pk>[0-9]+)/add/$', views.add_cart, name='add_cart'),
    url(r'^cart/(?P<pk>[0-9]+)/remove/$', views.remove_cart, name='remove_cart'),
    url(r'^cart/checkout$', views.checkout, name='checkout'),
]


