''' taskapi url '''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/contact/$', views.contact_list, name = 'contact_list'),
    url(r'^api/v1/contact/(?P<contact_id>[0-9])/$', views.contact_update_delete, name = 'contact_update_delete'),

]
