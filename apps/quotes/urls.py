
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login ),
    url(r'^logout$', views.logout ),
    url(r'^quotes$', views.quotes),  #takes the logged in/registered user to the main page/quote dashboard
    url(r'^contribute$', views.contribute),
    url(r'^addToFavs/(?P<quote_id>\d+)$', views.addToFavs),
    url(r'^removeFromFavs/(?P<quote_id>\d+)$', views.removeFromFavs),
    url(r'^users/(?P<user_id>\d+)$', views.show)
    
]    