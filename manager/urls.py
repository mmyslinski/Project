from django.conf.urls import url
from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.Detail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/odbior$', views.pickup_view, name='pickup'),
    url(r'^(?P<pk>\d+)/potwierdzenie_odbioru$', views.PickupConfirmationView.as_view(), name='confirmation'),
    url(r'^dodaj$', views.AddItem.as_view(), name='add_item'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
]
