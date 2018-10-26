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

        response = self.client.post(
            '/api/v1/products',
            data=json.dumps(
                self.product),
            content_type=self.content_type)
        data = json.loads(response.get_data().decode('UTF-8'))    
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, {"message": "Product has been added"})        

    def test_user_can_get_product_by_id(self):
        """Test user can get a product by id"""

        response = self.client.get(
            "/api/v1/products/1",
            content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_if_name_is_blank(self):
        """Test if name is blank"""

        payload = {
            "name": "",
            "category": "snack",
            "quantity": "123",
            "minimum_inventory_quantity": 30,
            "price": "12345"}

        response = self.client.post(
            '/api/v1/products',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "Name is required"})

    def test_if_category_is_blank(self):
        """Test if category is blank"""

        payload = {
            "name": "Popcorn",
            "category": "",
            "quantity": "123",
            "minimum_inventory_quantity": "30",
            "price": "12345"}

        response = self.client.post(
            '/api/v1/products',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "Category is required"})

    def test_if_quantity_is_blank(self):
        """Test if quantity is blank"""

        payload = {
            "name": "Popcorn",
            "category": "snacks",
            "quantity": "",
            "minimum_inventory_quantity": "30",
            "price": "12345"}

        response = self.client.post(
            '/api/v1/products',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "Quantity is required"})

    def test_if_minimum_inventory_quantity_is_blank(self):
        """Test if minimum inventory quantity is blank"""

        payload = {
            "name": "Popcorn",
            "category": "snacks",
            "quantity": "123",
            "minimum_inventory_quantity": "",
            "price": "12345"}

        response = self.client.post(
            '/api/v1/products',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "minimum inventory quantity is required"})                                    

    def test_if_price_is_blank(self):
        """Test if price is blank"""

        payload = {
            "name": "Popcorn",
            "category": "snacks",
            "quantity": "123",
            "minimum_inventory_quantity": "30",
            "price": ""}

        response = self.client.post(
            '/api/v1/products',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "Price is required"})
              