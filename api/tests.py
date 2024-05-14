"""api test"""
# set environment vars
import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShareAndTalk.settings')
setup()
# import
import unittest
from hashlib import md5
from django.urls import reverse
from django.core import mail
from django.conf import settings
from django.test import TestCase

from users.models import Profile
