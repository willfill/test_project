# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from test_project.accounts.forms import RegByPhoneForm
from test_project.accounts.models import Profile

def reg_by_phone(request):
    reg_form = RegByPhoneForm()
    if request.method == 'POST':
        reg_form = RegByPhoneForm(request.POST)
        if reg_form.is_valid():
            profile, message = Profile.create_profile(phone=reg_form.cleaned_data['phone'], password=reg_form['password'])
            return HttpResponse(simplejson.dumps({'result': message}), content_type='application/json')
    return render(request, 'accounts/reg_by_phone.html', {'reg_form': reg_form})