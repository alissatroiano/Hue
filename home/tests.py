from django.test import TestCase


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

    def test_this_thing_works2(self):
        self.assertEqual(1, 0)

    def test_this_thing_works3(self):
        self.assertEqual(1, 1)

    def test_this_thing_work4(self):
        self.assertEqual(1, 30)
