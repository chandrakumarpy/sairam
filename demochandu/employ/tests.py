from django.test import TestCase
from rest_framework import status
from employ.models import *
from rest_framework.response import Response
from django.urls import reverse




class EmployTest(TestCase):

    def setUp(self):
        Employ.objects.create(
            first_name='sai', last_name="chandu", date_of_birth='2022-02-08', gender ="M")
        Employ.objects.create(
            first_name='sai1', last_name="chandu1", date_of_birth='2019-02-08', gender ="M")
        
    def test_creation(self):
        self.assertEqual(Response.status_code, status.HTTP_200_OK)


    def test_check_data(self):
        self.assertEqual(Employ.objects.count(), 2)
        self.assertEqual(Employ.objects.filter()[1].first_name, 'sai1')

