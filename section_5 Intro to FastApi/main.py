# swagger-ui is in built in fast api
from fastapi import FastAPI

app = FastAPI()

to_dos = [
    {
        "id": 1,
        "title": "Buy Milk",
        "description": "Roj Subah one glass milk",
        "category": "urgent",
    },
    {
        "id": 2,
        "title": "Buy Chocolate",
        "description": "Daily Milk Please",
        "category": "not urgent",
    },
    {
        "id": 3,
        "title": "Buy Snacks",
        "description": "Kachori Samosa",
        "category": "not urgent",
    },
    {
        "id": 4,
        "title": "Buy Brain",
        "description": "Brain is important",
        "category": "urgent",
    },
]


@app.get("/todos")
async def get_all_todos():
    return to_dos


# @app.get("/todos/")
# async def get_all_todos():
#     return {"data":"Backchodi"}


@app.get("/todos/{_id}")
async def get_todo(_id, category=True):
    _id = int(_id)
    for to_do in to_dos:
        if to_do["id"] == _id and (to_do["category"] == category or category):
            return {"data": to_do}
    return {"err": "Not Found"}
