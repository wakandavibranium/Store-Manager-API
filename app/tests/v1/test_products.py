import unittest
import json

# Local import
from ... import create_app


class ProductTestCase(unittest.TestCase):

    def setUp(self):
        """Initialize Flask app and declare variables to
        be used before running every test"""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.content_type = "application/json"
        self.product = {
            'name': 'Popcorn',
            'category': 'Snacks',
            'quantity': 150,
            "minimum_inventory_quantity": 5,
            'price': 20}

    def tearDown(self):
        """Empty the product dictionary after running every test"""

        self.product = {}

    def test_user_can_get_all_products(self):
        """Test user can get all products"""

        response = self.client.get(
            "/api/v1/products",
            content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_add_a_product(self):
        """Test that a product can be added"""

        posted_product = self.client.post(
            '/api/v1/products',
            data=json.dumps(
                self.product),
            content_type=self.content_type)
        self.assertEqual(posted_product.status_code, 201)

    def test_user_can_get_product_by_id(self):
        """Test user can get a product by id"""

        response = self.client.get(
            "/api/v1/products/1",
            content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
