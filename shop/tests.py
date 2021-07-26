from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):

    def test_product_form_is_valid(self):
        form = ProductForm({
            'title': 'Test Product',
            'price': '1.00',
            'qty': '1'})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.is_bound)
        self.assertEqual(form.cleaned_data['title'], 'Test Product')

    def test_product_form_is_invalid(self):
            form = ProductForm({
				'title': '',
				'description': '',
				'price': '',
				'quantity': '',
			})
            self.assertFalse(form.is_valid())
            self.assertTrue(form.is_bound)
            self.assertEqual(form.errors['title'], ['This field is required.'])
