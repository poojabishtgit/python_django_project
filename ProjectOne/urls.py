
from django.contrib import admin
from django.urls import path
from apps.index.views import index,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/index',index),
    path('/register',register)
]