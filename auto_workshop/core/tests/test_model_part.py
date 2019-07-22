from datetime import datetime

from django.test import TestCase

from auto_workshop.core.models import Vehicle, Order, OrderPart


class PartModelTest(TestCase):

    def setUp(self):
        date = datetime.now()
        v1 = Vehicle.objects.create(plate="LVW4678", brand="Honda")
        self.order = Order.objects.create(vehicle=v1, date=date)

    def test_create(self):
        part = OrderPart.objects.create(order=self.order,
                                        quantity=1,
                                        description='virabrequim',
                                        unity=1500.78,
                                        amount=1500.78)
        self.assertTrue(OrderPart.objects.exists())
