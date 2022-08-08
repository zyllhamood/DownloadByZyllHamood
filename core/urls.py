from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('',index,name='index-home'),
    path('admin/', admin.site.urls),

]
