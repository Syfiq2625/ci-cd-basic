from fastapi import FastAPI, HTTPException
from src.api.models import Item

app = FastAPI(title="Project 9 API")

# In-memory database (karena tanpa database beneran)
db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Project 9 API"}

@app.post("/items/", status_code=201)
def create_item(item: Item):
    db.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
