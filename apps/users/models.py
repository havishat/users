# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAILisnotvalid = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be more than 5 characters"
        if not postData['first_name'].isalpha():
            errors["first_name"] = 'First name must be all letters'
        if not postData['last_name'].isalpha():
            errors["last_name"] = 'Last name must be all letters'
        if len(postData['last_name'])< 2 :
            errors["last_name"] = 'Last name must be at least two characters'
        if not EMAILisnotvalid.match(postData['email']):
            errors["email_name"] = "Invalid Email Address!"
        return errors
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()