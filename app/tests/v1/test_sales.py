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
            'number_of_items_sold': 12,
            'transaction_amount': 34000,
            'date_created': datetime.now,
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

        posted_sale = self.client.post(
            '/api/v1/sales',
            data=json.dumps(
                self.sale),
            content_type=self.content_type)
        self.assertEqual(posted_sale.status_code, 201)
