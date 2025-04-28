from fastapi import FastAPI, HTTPException
import uuid
import logic
from models import Receipt

app = FastAPI()

# In-memory "database"
items = {}

@app.post("/receipts/process")
def create_item(receipt: Receipt):
    points = logic.process(receipt)
    receipt_id = str(uuid.uuid4())
    items[receipt_id] = points
    return {"id": receipt_id}

@app.get("/receipts/{id}/points")
def read_item(id: str):
    item = items.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'points': item}