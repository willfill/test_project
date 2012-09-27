# -*- coding: UTF-8 -*-
from django import forms
from django.core.exceptions import ValidationError

class RegByPhoneForm(forms.Form):
    phone = forms.IntegerField(label=u'Телефон')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'Повтор пароля', widget=forms.PasswordInput)

    def clean(self):
        data = super(RegByPhoneForm, self).clean()
        if data.get('password') != data.get('password2'):
            raise ValidationError(u'Пароль и его повтор не совпадают')
        else:
            return data