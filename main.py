from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="static")

items = {}
item_id_counter = 0

# Route to list all items
@app.get("/items")
def list_items():
    return items

# Route to list a specific item
@app.get("/items/{item_id}")
def list_item(item_id: int):
    if str(item_id) in items:
        return {"item_id": item_id, "item": items[str(item_id)]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Route to add an item
@app.post("/items")
def add_item(item: str):
    global item_id_counter
    item_id_counter += 1
    item_id = str(item_id_counter)
    items[item_id] = item
    return {"item_id": item_id, "item": item}

# Route to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if str(item_id) not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[str(item_id)]
    return {"result": "Item deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")