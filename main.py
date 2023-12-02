from fastapi import FastAPI
import uvicorn
import dotenv
import os
from database.connection import db
from tables.models import *

from fastapi.middleware.cors import CORSMiddleware

dotenv.load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #accepts requests from any origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/restaurants")
def get_restaurants():
    return db.query(Restaurants).limit(20).all()

@app.get("/restaurant/menu/{id}")
def get_menu(id: int):
    results = db.query(MenuCategories, MenuItems).select_from(Restaurants).filter(Restaurants.id == id).join(MenuCategories, Restaurants.id == MenuCategories.restaurants_id).join(MenuItems, MenuCategories.id == MenuItems.menu_categories_id).all()
    h = {}

    class ItemsPerCategory:
        def __init__(self, details):
            self.menu_category = details
            self.menu_items = []

    for category, item in results:
        if category.name not in h:
            h[category.name] = ItemsPerCategory(category)
            h[category.name].menu_items.append(item)
            continue
        h[category.name].menu_items.append(item)
          
    return [v for _, v in h.items()]

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)