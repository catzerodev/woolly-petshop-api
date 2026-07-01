from app.models.category_model import Category
from app.schemas.category_schema import CategorySchema
from db import db


class CategoryService:

    def create(self, data: CategorySchema) -> Category:

        category = Category(
            name=data.name,
            description=data.description
        )

        db.session.add(category)

        db.session.commit()

        return category