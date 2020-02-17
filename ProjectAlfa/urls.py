from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #include the all urls from bank app
    path('',include('bank.urls'))

]