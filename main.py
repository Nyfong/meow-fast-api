from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from fake_db import fake_items  # Import the fake_db list
from pydantic import BaseModel

app = FastAPI()
# Pydantic model for input (only name, as id is auto-incremented)
class ItemCreate(BaseModel):
    name: str

# Pydantic model for output (includes id and name)
class Item(BaseModel):
    id: int
    name: str
    
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

#the scalar view ui
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=app.openapi_url,
        # Avoid CORS issues (optional)
        scalar_proxy_url="https://proxy.scalar.com",
    )


#let return array

@app.get("/items")
async def read_items():
    return fake_items

#post 

@app.post("/items")
async def create_item(item: ItemCreate):
    # Auto-increment ID: Find the maximum ID in fake_db and add 1
    max_id = max([item["id"] for item in fake_items], default=0)
    new_id = max_id + 1
    # Create new item dictionary
    new_item = {"id": new_id, "name": item.name}
    fake_items.append(new_item)
    return new_item