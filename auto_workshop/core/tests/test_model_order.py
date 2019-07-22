from datetime import datetime

from django.test import TestCase

from auto_workshop.core.models import Vehicle, Order


class OrderModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(plate="LVW4678", brand="Honda")

    def test_date(self):
        service_date = datetime.now()
        service = Order.objects.create(vehicle=self.vehicle, date=service_date)
        self.assertTrue(Order.objects.exists())

    def test_str(self):
        service_date = datetime.now()
        service = Order.objects.create(vehicle=self.vehicle, date=service_date)
        self.assertEqual('Honda - LVW4678', str(service))

    def test_order(self):
        service_date = datetime.now()
        service = Order.objects.create(vehicle=self.vehicle,
                                       date=service_date,
                                       odometer=139090)
        self.assertTrue(Order.objects.exists())

    def test_odometer_can_be_blank(self):
        field = Order._meta.get_field('odometer')
        self.assertTrue(field.blank)

    def test_odometer_can_be_null(self):
        field = Order._meta.get_field('odometer')
        self.assertTrue(field.null)
