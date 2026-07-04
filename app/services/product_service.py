from app.models.product_model import Product
from app.schemas.product_schema import ProductSchema
from db import db


class ProductService:

    def create(self, data: ProductSchema) -> Product:

        product = Product(
            name=data.name,
            description=data.description,
            price=data.price,
            stock=data.stock,
            image_url=data.image_url,
            category_id=data.category_id
        )

        db.session.add(product)
        db.session.commit()

        return product

    def get_all(self) -> list[Product]:

        products = Product.query.filter_by(
            is_active=True
        ).all()

        return products

    def get_by_id(self, product_id: int) -> Product | None:

        product = Product.query.get(product_id)

        return product

    def update(self, product_id: int, data: ProductSchema) -> Product | None:

        product = self.get_by_id(product_id)

        if product is None:
            return None

        product.name = data.name
        product.description = data.description
        product.price = data.price
        product.stock = data.stock
        product.image_url = data.image_url
        product.category_id = data.category_id

        db.session.commit()

        return product

    def delete(self, product_id: int) -> bool:

        product = self.get_by_id(product_id)

        if product is None:
            return False

        product.is_active = False

        db.session.commit()

        return True