from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_entries, name='show_entries'),
    url(r'^add$', views.add_entry, name='add_entry'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]
