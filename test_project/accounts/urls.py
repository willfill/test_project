# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from test_project.accounts.views import reg_by_phone


urlpatterns = patterns('',
    url(r'reg-by-phone/$', reg_by_phone, name='reg_by_phone'),
)