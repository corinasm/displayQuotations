
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login ),
    url(r'^logout$', views.logout ),
    url(r'^quotes$', views.quotes),  #takes the logged in/registered user to the main page/quote dashboard
    url(r'^users/(?P<user_id>\d+)$', views.show),      #show quotes posted by user with user_id in a new apge 
    #url(r'^quotes/(?P<user_id>\d+)/contribute$', views.contribute) #user adds a new quote 
    url(r'^contribute$', views.contribute),
    url(r'^display_quotes$', views.display_quotes),
    url(r'^add_to_fav/?P<user_id>\d+)$', views.add_to_fav),
    url(r'^removw_from_fav/?P<user_id>\d+)$', views.remove_from_fav),
]