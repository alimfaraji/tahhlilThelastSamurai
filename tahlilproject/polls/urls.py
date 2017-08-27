from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'), #todo done
    url(r'^financial/bill/$', views.payBills, name='bill'),
    url(r'^financial/charge/$', views.payCharges, name='charge'),
    url(r'^index/removeFromDashbord/([0-9]+)/$', views.removeFromDashbord, name='removeFromDashbord'),
    url(r'^neighbors/$', views.neighbors, name='neighbors'),
    url(r'^facilities/$', views.facilities, name='facilities'),
    url(r'^facilities/([a-z]+)/([0-9]+)/$', views.reserveFacility, name='reserveFacility'),
    url(r'^facilities/delete/([a-z]+)/([a-z]+)/([0-9]+)/$', views.deleteReservations, name = 'deleteReservation'),
    url(r'^facilities/remove/([a-z]+)/([0-9]+)/$', views.removeFacility, name='removeFacility'),
    url(r'^neighbors/remove/([a-z]+)$', views.removeNeighbor, name = 'removeNeighbor'),
    url(r'^neighbors/detailsNeighbor/([a-z]+)$', views.detailsNeighbor, name='detailsNeighbor'),
    url(r'^neighbors/detailsNeighbor/warnCharge/([a-z]+)/([0-9]+)/$', views.warnCharge, name = 'warnCharge'),
    url(r'^neighbors/detailsNeighbor/warnBill/([a-z]+)/([0-9]+)/$', views.warnBill, name = 'warnBill'),
    url(r'^owner/$', views.owner, name='owner'),
    url(r'^financial/tenant/$', views.tenant, name='tenant'),
    # url(r'^(?P<id>[0-9]+)/financial/(?P<type>[\w\-]+)/$' , views.financial , name='financial'),
    # url(r'^(?P<id>[0-9]+)/financial/(?P<type>[\w\-]+)/pay/(?P<pay>[0-9]+)/$', views.pay, name='pay'),
    # url(r'^(?P<id>[0-9]+)/reservation/(?P<reserve>[0-9]+)/$', views.reservation, name='reservation'),
    # url(r'^(?P<id>[0-9]+)/neighbors/$', views.neighbors, name='neighbors'),
    # url(r'^(?P<id>[0-9]+)/neighbors/add/$', views.neighbors_add, name='neighbors_add'),
    # url(r'^(?P<id>[0-9]+)/guest/(?P<guest_id>[\w\-]+)/$', views.guest, name='guest'),
    # url(r'^(?P<id>[0-9]+)/guest/(?P<guest_id>[\w\-]+)/request$', views.guest_request, name='guest_request'),
    # url(r'^(?P<id>[0-9]+)/validation/$', views.validation, name='validation'),

]