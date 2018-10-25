from flask import request
from flask_restplus import Resource, Namespace, fields

# Local import
from .models import ProductModel

namespace_1 = Namespace("products", description="End points for products")


@namespace_1.route('/')
class Products(Resource):
    """Get products and create products"""

    def get(self):
        """Get all products"""

        products_list = []

        # Loop through all the products
        for p in ProductModel.products:
            products_list.append(p.get_product_details())

        return {"message": "Success", "data": products_list}, 200
