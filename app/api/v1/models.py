class ProductModel:
    """The class contains details of a product"""

    # unique identifier
    product_id = 1

    # list of products
    products = []

    def __init__(
            self,
            name,
            category,
            quantity,
            minimum_inventory_quantity,
            price):
        """Initialize class constructor with product details"""

        self.id = ProductModel.product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.minimum_inventory_quantity = minimum_inventory_quantity
        self.price = price
        # Increment product_id by 1 every time this class is instantiated
        ProductModel.product_id += 1

    @classmethod
    def get_a_product_by_id(cls, id):
        """Get a single product"""

        # Loop through the list of products
        for product in cls.products:
            # Check if the product id supplied exists
            if id == product.id:
                return product

    def get_product_details(self):
        """Return the product as a dictionary"""

        return dict(
            id=self.id,
            name=self.name,
            category=self.category,
            quantity=self.quantity,
            minimum_inventory_quantity=self.minimum_inventory_quantity,
            price=self.price
        )
