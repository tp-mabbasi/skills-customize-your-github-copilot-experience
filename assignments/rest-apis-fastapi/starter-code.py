from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="My Item API")

# -------------------------------------------------------------------
# Data model
# -------------------------------------------------------------------

class Item(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: str = Field("", max_length=200)

# In-memory "database"
items: List[Item] = []

# -------------------------------------------------------------------
# TODO: Implement the endpoints below
# -------------------------------------------------------------------

# GET /items — return all items
@app.get("/items", response_model=List[Item])
def get_items():
    # TODO: return the list of items
    pass

# GET /items/{item_id} — return a single item or 404
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    # TODO: find the item with the matching id
    # Hint: raise HTTPException(status_code=404, detail="Item not found") if missing
    pass

# POST /items — add a new item
@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    # TODO: append the item to the list and return it
    pass

# PUT /items/{item_id} — update an existing item or 404
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    # TODO: find the item, update its fields, and return it
    pass

# DELETE /items/{item_id} — remove an item or 404
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # TODO: find and remove the item
    pass
