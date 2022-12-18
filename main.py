from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Hello World!
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Read the items id and retun it
    """
    return {"item_id": item_id, "q": q}
