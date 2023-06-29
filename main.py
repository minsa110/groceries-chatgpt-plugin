from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import redis

redis_client = redis.StrictRedis(host='0.0.0.0', port=6379, db=0, decode_responses=True)

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="static")

# Route to list all items
@app.get("/items")
def list_items():
    items = {}
    for key in redis_client.keys():
        if key != 'item_id':
            items[key] = "["+key+"] "+str(redis_client.get(key))
    return items

# Route to list a specific item
@app.get("/items/{item_id}")
def list_item(item_id: int):
    item = redis_client.get(str(item_id))
    if item:
        return {"item_id": item_id, "item": item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Route to add a item
@app.post("/items")
def add_item(item: str):
    # Generate a unique item_id
    item_id = redis_client.incr('item_id')
    redis_client.set(str(item_id), item)
    return {"item_id": item_id, "item": item}

# Route to delete a item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if not redis_client.exists(str(item_id)):
        raise HTTPException(status_code=404, detail="Item not found")
    redis_client.delete(str(item_id))
    return {"result": "Item deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")