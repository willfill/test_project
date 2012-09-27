# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    sex_choices = ((1, u'Муж'), (2, 'Жен'))

    user = models.OneToOneField(verbose_name=u'Пользователь', null=False, blank=False, related_name=u'profile', to=User)
    phone = models.CharField(verbose_name=u'Телефон', max_length='20')
    vk_id = models.CharField(verbose_name=u'ВКонтакте ID', max_length='20', null=True, blank=True)
    facebook_id = models.CharField(verbose_name=u'ВКонтакте ID', max_length='20', null=True, blank=True)
    skype_id = models.CharField(verbose_name=u'Skype ID', max_length='50', null=True, blank=True)
    first_name = models.CharField(verbose_name=u'Имя', max_length='50', null=True, blank=True)
    second_name = models.CharField(verbose_name=u'Фамилия', max_length='50', null=True, blank=True)
    middle_name = models.CharField(verbose_name=u'Отчество', max_length='50', null=True, blank=True)
    sex = models.PositiveSmallIntegerField(verbose_name=u'Пол', choices=sex_choices, null=True, blank=True)
    birth_date = models.DateField(verbose_name=u'Дата рождения', null=True, blank=True)
    register_date = models.DateTimeField(verbose_name=u'Дата регистрации', auto_now_add=True)
    activation_date = models.DateTimeField(verbose_name=u'Дата активации', null=True, blank=True)
    is_registered = models.BooleanField(verbose_name=u'Зарегистрирован?', default=False)

    def __unicode__(self):
        return u'profile_ID-% %s %s' % (self.id, self.first_name, self.second_name)

    @classmethod
    def create_profile(cls, phone, password):
        phone_username = 'phone_%s' % phone
        try:
            User.objects.get(username=phone_username)
            return None, u'already exist'
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=phone_username, password=password)
            return Profile.objects.create(user=new_user, phone=phone), u'success'