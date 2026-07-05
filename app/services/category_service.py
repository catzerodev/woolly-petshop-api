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

    def get_all(self) -> list[Category]:

        categories = Category.query.filter_by(
            is_active=True
        ).all()

        return categories
    
    def get_by_id(self, category_id: int) -> Category:
        
        category = Category.query.filter_by(
            id=category_id,
            is_active=True
        ).first()

        return category
    
    def update(self, category_id: int, data: CategorySchema) -> Category:
        category = self.get_by_id(category_id)
        category.name = data.name
        category.description = data.description
        db.session.commit() 
        
        return category
    
    def delete(self, category_id: int) -> bool:
        category = self.get_by_id(category_id)
        if category is None:
            return False
        category.is_active = False
        db.session.commit()

        return True
        
    
    
    