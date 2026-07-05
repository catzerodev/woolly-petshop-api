from pydantic import BaseModel
class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    image_url: str | None = None
    category_id: int
    
