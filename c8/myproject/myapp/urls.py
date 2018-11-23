from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^submit$', views.submit, name='submit'),
]