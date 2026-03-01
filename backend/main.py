from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import subprocess
import uvicorn

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI()

# CORS для Vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

items = []
current_id = 1


@app.get("/api/items")
def get_items():
    return items


@app.post("/api/items")
def create_item(item: Item):
    global current_id
    new_item = item.dict()
    new_item["id"] = current_id
    items.append(new_item)
    current_id += 1
    return new_item


@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    subprocess.Popen(["npm", "run", "dev"], cwd=str(FRONTEND_DIR), shell=True)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)