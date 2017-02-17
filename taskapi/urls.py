''' taskapi url '''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/contact/$', views.contact_list, name = 'contact_list'),

]
