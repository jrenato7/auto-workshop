from datetime import datetime

from django.test import TestCase

from auto_workshop.core.models import Vehicle


class VehicleModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(plate="MEU2650",
                               brand="Peugeot",
                               model="206 1.4",
                               year=2007,
                               color="silver")
        self.vehicle.save()

    def test_create(self):
        self.assertTrue(Vehicle.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.vehicle.created_at, datetime)

    def test_str(self):
        self.assertEqual('Peugeot - MEU2650', str(self.vehicle))

