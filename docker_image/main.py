from typing import Union

from fastapi import FastAPI

app = FastAPI()

items = {}
names = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_item():
    return {"items": items}


@app.get("/names/")
def read_item():
    return {"names": names}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
