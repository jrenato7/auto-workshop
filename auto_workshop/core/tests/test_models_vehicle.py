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

    def test_model_can_be_blank(self):
        field = Vehicle._meta.get_field('model')
        self.assertTrue(field.blank)

    def test_year_can_be_blank(self):
        field = Vehicle._meta.get_field('year')
        self.assertTrue(field.blank)

    def test_color_can_be_blank(self):
        field = Vehicle._meta.get_field('color')
        self.assertTrue(field.blank)

    def test_model_can_be_null(self):
        field = Vehicle._meta.get_field('model')
        self.assertTrue(field.null)

    def test_year_can_be_null(self):
        field = Vehicle._meta.get_field('year')
        self.assertTrue(field.null)

    def test_color_can_be_null(self):
        field = Vehicle._meta.get_field('color')
        self.assertTrue(field.null)

    def test_odometer_can_be_blank(self):
        field = Vehicle._meta.get_field('odometer')
        self.assertTrue(field.blank)

    def test_odometer_can_be_null(self):
        field = Vehicle._meta.get_field('odometer')
        self.assertTrue(field.null)
