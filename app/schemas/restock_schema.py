from pydantic import BaseModel, Field


class RestockSchema(BaseModel):

    quantity: int = Field(gt=0)