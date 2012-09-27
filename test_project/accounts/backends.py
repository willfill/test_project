# -*- coding: UTF-8 -*-

# Registration backends
class BaseRegistration(object):

    def __init__(self, *args, **kwargs):
        pass

    def process_registration(self, **credentials):
        pass

    def notification(self):
        pass