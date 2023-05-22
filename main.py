from fastapi import FastAPI
from db import Base, engine
from routers import authentication_router, category_router, subcategory_router, product_router, image_router


app = FastAPI()


Base.metadata.create_all(engine)


app.include_router(authentication_router, tags=['Authentication'])
app.include_router(category_router, tags=['Category'])
app.include_router(subcategory_router, tags=['Sub-Category'])
app.include_router(product_router, tags=['Product'])
app.include_router(image_router, tags=['Image'])