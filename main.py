from fastapi import FastAPI
from pydantic import BaseModel
import redis
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the .well-known directory to path /.well-known
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="static")
r = redis.Redis(host='localhost', port=6379, db=0)

class Item(BaseModel):
    name: str

@app.post("/items/")
async def create_item(item: Item):
    item_id = r.incr("item_id")
    r.set(f"item:{item_id}", item.name)
    return {"item_id": item_id, "name": item.name}

@app.get("/items/")
async def read_items():
    items = []
    for key in r.keys("item:*"):
        item_id = key.decode().split(":")[1]
        item_name = r.get(key).decode()
        items.append({"item_id": item_id, "name": item_name})
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item_name = r.get(f"item:{item_id}")
    if item_name is None:
        return {"error": "Item not found"}
    return {"item_id": item_id, "name": item_name.decode()}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if r.delete(f"item:{item_id}") == 0:
        return {"error": "Item not found"}
    return {"message": "Item deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)