from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

print(fake_items_db)
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip : skip + limit]