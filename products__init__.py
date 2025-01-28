from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        return Product(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            cost=data["cost"],
            qty=data.get("qty", 0)  # Use `get()` to handle missing `qty` keys safely
        )

def list_products() -> list[Product]:
    return [Product.load(product) for product in dao.list_products()]

def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))

def add_product(product: Product) -> None:
    dao.add_product(vars(product))  # Converts Product object to a dictionary

def update_qty(product_id: int, qty: int) -> None:
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, qty)
