import unittest
from datetime import datetime
import json

# Local import
from ... import create_app


class SaleTestCase(unittest.TestCase):

    def setUp(self):
        """Initialize Flask app and declare variables to
        be used before running every test"""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.content_type = "application/json"
        self.sale = {
            "number_of_items_sold": 12,
            "transaction_amount": 34000,
            "created_by": "John Doe"}

    def tearDown(self):
        """Empty the sale dictionary after running every test"""

        self.sale = {}

    def test_admin_can_get_all_sales_records(self):
        """Test admin can get all sales"""

        response = self.client.get(
            "/api/v1/sales",
            content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_add_a_sale(self):
        """Test that a sale can be added"""

        response = self.client.post(
            '/api/v1/sales',
            data=json.dumps(
                self.sale),
            content_type=self.content_type)
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, {"Message": "Sale has been added"})

    def test_user_can_get_sale_record_by_id(self):
        """Test user can get a sale by id"""

        response = self.client.get(
            "/api/v1/sales/1",
            content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_if_number_of_items_sold_is_blank(self):
        """Test if number_of_items_sold is blank"""

        payload = {
            "number_of_items_sold": "",
            "transaction_amount": 2500,
            "created_by": "John Doe"}

        response = self.client.post(
            '/api/v1/sales',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "No. of items sold is required"})

    def test_if_number_of_items_sold_is_not_integer(self):
        """Test if number_of_items_sold is not integer"""

        payload = {
            "number_of_items_sold": "ewrew213",
            "transaction_amount": 2500,
            "created_by": "John Doe"}

        response = self.client.post(
            '/api/v1/sales',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            data, {
                "message": "No. of items sold must be an integer"})

    def test_if_transaction_amount_is_blank(self):
        """Test if transaction_amount is blank"""

        payload = {
            "number_of_items_sold": 12345,
            "transaction_amount": "",
            "created_by": "John Doe"}

        response = self.client.post(
            '/api/v1/sales',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "Transaction amount is required"})

    def test_if_transaction_amount_is_not_integer(self):
        """Test if transaction_amount is not integer"""

        payload = {
            "number_of_items_sold": 12345,
            "transaction_amount": "fgfd34",
            "created_by": "John Doe"}

        response = self.client.post(
            '/api/v1/sales',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            data, {
                "message": "Transaction amount must be an integer"})

    def test_if_created_by_is_blank(self):
        """Test if created_by is blank"""

        payload = {
            "number_of_items_sold": 12,
            "transaction_amount": 78765,
            "created_by": ""}

        response = self.client.post(
            '/api/v1/sales',
            content_type=self.content_type,
            data=json.dumps(payload))
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data, {"message": "Created by field is required"})
