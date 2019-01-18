"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from m11_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

#Odler version for stepik
from django.conf.urls import include, url

urlpatterns = [
    url('^$', include('qa.urls')),
    url('^login/', include('qa.urls'), name='login'),
    url('^signup/', include('qa.urls'), name='signup'),
    url('^ask/', include('qa.urls'), name='ask'),
    url('^popular/', include('qa.urls'), name='popular'),
    url('^new/', include('qa.urls'), name='new'),
]

'''
from django.urls import path, include

urlpatterns  = [
    path('', include('qa.urls')),
    path('login/', include('qa.urls'), name='login'),
    path('signup/', include('qa.urls'), name='signup'),
    path('ask/', include('qa.urls'), name='ask'),
    path('popular/', include('qa.urls'), name='popular'),
    path('new/', include('qa.urls'), name='new'),
]
'''