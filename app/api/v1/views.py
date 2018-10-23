
from flask import request
from flask_restplus import Resource, Namespace, fields

# Local imports
from .models import ProductModel, SaleModel, UserModel

namespace_1 = Namespace("products", description="End points for products")
namespace_2 = Namespace("sales", description="End points for sales")
namespace_3 = Namespace("auth/signup", description="End points for signup")
namespace_4 = Namespace("auth/login", description="End point for login")

product = namespace_1.model('Products', {
    "name": fields.String(required=True, description="Product name"),
    "category": fields.String(required=True, description="Product category"),
    "quantity": fields.Integer(required=True, description="Quantity"),
    "minimum_inventory_quantity": fields.Integer(description="Mininum Inventory Quantity"),
    "price": fields.Integer(required=True, description="Price")
})

sale = namespace_2.model('Sales', {
    'number_of_items_sold': fields.Integer(required=True, description="No. of items sold"),
    'transaction_amount': fields.Integer(required=True, description="Transaction Amount"),
    'date_created': fields.String(required=True, description="Date sale was created"),
    'created_by': fields.String(required=True, description="User who created sale")
})

user = namespace_3.model('User Registration', {
    'name': fields.String(required=True, description="Your name"),
    'email': fields.String(required=True, description="Your email"),
    'phone': fields.Integer(required=True, description="Phone number"),
    'role': fields.String(required=True, description="Your role"),
    'password': fields.String(required=True, description="Enter password")
})

user_login = namespace_4.model('User Login', {
    'email': fields.String(required=True, description="Your email"),
    'password': fields.String(required=True, description="Your password")
})


@namespace_1.route('/')
class Products(Resource):
    """Get products and create products"""

    def get(self):
        """Get all products"""

        products_list = []

        # Check if the products list has a record
        if len(ProductModel.products) > 0:
            # Loop through all the products
            for p in ProductModel.products:
                products_list.append(p.get_product_details())
            return {"Message": "Success", "data": products_list}, 200
        else:
            return {"Message": "No products were found"}, 404

    @namespace_1.expect(product)
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
        """Get a product by id"""

        search_product = ProductModel.get_a_product_by_id(id)

        # Check if there is a product
        if search_product:
            return {"Product": search_product.get_product_details()}, 200
        elif not search_product:
            return {"Message": "Product not found"}, 404


@namespace_2.route('/')
class Sales(Resource):
    """Get sales and create sales"""

    def get(self):
        """Get all sales"""

        sales_list = []

        # Check if the sales list has a record
        if len(SaleModel.sales) > 0:
            # Loop through all the sales records
            for s in SaleModel.sales:
                sales_list.append(s.get_sale_details())
            return {"Message": "Success", "data": sales_list}, 200
        else:
            return {"Message": "No sales were found"}, 404

    @namespace_2.expect(sale)
    def post(self):
        """Add a sale"""

        data = request.get_json(force=True)
        add_sale = SaleModel(data['number_of_items_sold'],
                             data['transaction_amount'],
                             data['date_created'],
                             data['created_by'])

        # Add the sale to the sales list
        SaleModel.sales.append(add_sale)
        return{"Message": "Sale has been added", "data": add_sale.get_sale_details()}, 201


@namespace_2.route('/<int:id>')
class Sale(Resource):

    def get(self, id):
        """Get one sale"""

        # search a sale record by id
        search_sale = SaleModel.get_a_sale_by_id(id)

        if search_sale:
            return {"Sale": search_sale.get_sale_details()}, 200
        elif not search_sale:
            return {"Message": "Sale not found"}, 404


@namespace_3.route('/')
class Signup(Resource):
    """The signup resource"""

    @namespace_3.expect(user)
    def post(self):
        """Sign up a user"""

        data = request.get_json(force=True)

        # search the user by email
        user_record = UserModel.get_a_user_by_email(data['email'])

        # check if the user is already registered
        if user_record:
            return {"message": "User {} already exists.".format(data['name'])}

        # register the user if he/she isn't registered
        if not user_record:
            signup_user = UserModel(data['name'],
                                    data['email'],
                                    data['phone'],
                                    data['role'],
                                    data['password'])

            # Add the signed up user
            UserModel.registered_users.append(signup_user)
            return {"message": "Sign up was successful"}, 201

    def get(self):
        """Get signed up users"""

        users = []

        # Check if the sales list has a record
        if len(UserModel.registered_users) > 0:
            # Loop through the users
            for u in UserModel.registered_users:
                users.append(u.get_user_details())
            return {"message": "Success", "data": users}, 200
        else:
            return {"Message": "No Users were found"}, 404


@namespace_4.route('/')
class Login(Resource):
    """User Login"""

    @namespace_4.expect(user_login)
    def post(self):
        """Login in a user"""

        data = request.get_json()

        # search the user by email
        user_record = UserModel.get_a_user_by_email(data['email'])

        # check if the user is already registered
        if user_record:
            # Check if the login credentials are valid
            if user_record.email == data['email'] and user_record.validate_password(
                    data['password']):
                return {"message": "Login Successful"}, 200
            return {"message": "Login Failed!"}, 401
        elif not user_record:
            return {"message": "You are not registered!. Please register"}, 403
