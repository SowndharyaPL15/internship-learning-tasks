from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Internship Items API")

class Item(BaseModel):
    name: str
    price: float
    description: str = ""

items = {}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/items/{id}")
def get_item(id: int):
    if id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return {"id": id, **items[id].model_dump()}

@app.post("/items", status_code=201)
def create_item(item: Item):
    item_id = max(items.keys(), default=0) + 1
    items[item_id] = item

    return {"id": item_id, **item.model_dump()}
