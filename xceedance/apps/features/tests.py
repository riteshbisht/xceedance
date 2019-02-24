from django.test import TestCase
from features.models import *
from .factories import FeatureFactory
# Create your tests here.

class TestFeatureApiView(TestCase):

    url = '/features/'

    def setUp(self):
        Feature.objects.all().delete()
        self.feature1 = FeatureFactory()
        self.feature2 = FeatureFactory()


    def test_get_200_reponse(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_all_fetaures(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_correct_keys(self):
        correct_keys = ('title', 'description', 'status', 'client', 'client_name' ,'priority', 'target_date', 'product', 'product_name')
        response = self.client.get(self.url)
        repsonse_keys = response.data[0].keys()
        for key in repsonse_keys:
            self.assertIn(key, correct_keys)

    def test_product_is_required(self):
        data = {
            'title': 'this is title',
            'description': 'this is description',
            'client': self.feature1.client.id,
            'target_date': '2019-15-11',
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['product'][0]), 'This field is required.')

    def test_client_is_required(self):
        data = {
            'title': 'this is title',
            'description': 'this is description',
            'target_date': '2019-15-11',
            'product': 1
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['client'][0]), 'This field is required.')


    def test_date_cannot_be_in_past(self):
        data = {
            'title': 'this is title',
            'description': 'this is description',
            'target_date': '2019-02-01',
            'product': 1
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['target_date'][0]), 'Date cannot be in the past')

    def test_client_does_not_exist(self):
        data = {
            'title': 'this is title',
            'description': 'this is description',
            'target_date': '2019-11-11',
            'client': 34,
            'product': 1
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['client'][0]), 'Invalid pk "34" - object does not exist.')
