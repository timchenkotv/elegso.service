from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('', lambda r: render(r, 'base.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]
