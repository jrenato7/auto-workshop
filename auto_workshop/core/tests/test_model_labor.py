from datetime import datetime

from django.test import TestCase

from auto_workshop.core.models import Vehicle, Order, OrderLabor


class LaborModelTest(TestCase):
    def setUp(self):
        date = datetime.now()
        v1 = Vehicle.objects.create(plate="LVW4678", brand="Honda")
        self.order = Order.objects.create(vehicle=v1, date=date)

    def test_description(self):
        labor = OrderLabor.objects.create(order=self.order,
                                          kind=OrderLabor.FIX,
                                          description='Retífica do virabrequim',
                                          price='350.57')
        self.assertTrue(OrderLabor.objects.exists())
