from pydantic import BaseModel


class BaseSchema(BaseModel):
    name_tm: str
    name_ru: str
    
    
class subCategorySchema(BaseSchema):
    category_id: int
    description_tm: str
    description_ru: str
    
class loginSchema(BaseModel):
    password: str
    
class registerSchema(loginSchema):
    username: str