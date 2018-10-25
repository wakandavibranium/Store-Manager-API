from flask import request
from flask_restplus import Resource, Namespace, fields

# Local import
from .models import ProductModel, SaleModel

namespace_1 = Namespace("products", description="End points for products")
namespace_2 = Namespace("sales", description="End points for sales")


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

    def post(self):
        """Add a product"""

        data = request.get_json(force=True)
        add_product = ProductModel(data['name'],
                                   data['category'],
                                   data['quantity'],
                                   data['minimum_inventory_quantity'],
                                   data['price'])

        # Add the product to the products list
        ProductModel.products.append(add_product)
        return{"message": "Product has been added", "data": add_product.get_product_details()}, 201


@namespace_1.route('/<int:id>')
class Product(Resource):
    def get(self, id):
        """Get one product"""

        search_product = ProductModel.get_a_product_by_id(id)
        return {"message": "Product Found",
                "data": search_product.get_product_details()}, 200


@namespace_2.route('/')
class Sales(Resource):
    """Get sales and create sales"""

    def get(self):
        """Get all sales"""

        sales_list = []

        # Loop through all the sales records
        for s in SaleModel.sales:
            sales_list.append(s.get_sale_details())

        return {"message": "Success", "data": sales_list}, 200

    def post(self):
        """Add a sale"""

        data = request.get_json(force=True)
        add_sale = SaleModel(data['number_of_items_sold'],
                             data['transaction_amount'],
                             data['date_created'],
                             data['created_by'])

        # Add the sale to the sales list
        SaleModel.sales.append(add_sale)
        return{"message": "Sale has been added", "data": add_sale.get_sale_details()}, 201
