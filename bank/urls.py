from django.urls import path
from django.conf.urls import url
from bank import views
from bank.views import home,bank
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    #api path
    url(r'^bank/',bank,name='bank'),
    #home path
    path('', home, name='home'),
]

