from datetime import datetime, UTC

from db import db


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)

    description = db.Column(db.String(255))

    price = db.Column(db.Numeric(10, 2), nullable=False)

    stock = db.Column(db.Integer, nullable=False, default=0)

    image_url = db.Column(db.String(500))

    is_active = db.Column(db.Boolean, nullable=False, default=True)

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    category = db.relationship(
        "Category",
        backref="products"
    )