"""DriftBottle URL Configuration

The `urlpatterns` list routes URLs to webApp. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function webApp
    1. Add an import:  from my_app import webApp
    2. Add a URL to urlpatterns:  url(r'^$', webApp.home, name='home')
Class-based webApp
    1. Add an import:  from other_app.webApp import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

#zxh, (?i) make url do not case sensitive
urlpatterns = [
    url(r'(?i)^register$', "WebUI.views.Register"),
    url(r'(?i)^login$', "WebUI.views.Login"),
    url(r'(?i)^mainInputForm$', "WebUI.views.mainInputForm"),
    url(r'(?i)^SingleOrderForm$', "WebUI.views.singleOrderForm"),
    url(r'(?i)^submitOrder', "WebUI.views.submitOrder"),
    url(r'(?i)^ShowResult$', "WebUI.views.showResult"),
]
