from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def test_get(self):
        resp = self.client.get(r('home'))
        self.assertEqual(200, resp.status_code)



