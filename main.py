from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

# TODO: Create GET /users/stats endpoint here
@app.get("/users/stats")
def get_user_stats():
    try:
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        todos = requests.get("https://jsonplaceholder.typicode.com/todos")
        parsed_users = users.json()
        parsed_todos = todos.json()
    except:
        return {"error": "an error while fetching has occurred"}

    results = []
    for user in parsed_users:
        user_stats = {"name": user["name"],
          "total_todos": 0,
          "completed_todos": 0,
          "completion_rate": 0}

        for todo in parsed_todos:
            if todo["userId"] == user["id"] and todo["completed"]:
                user_stats["total_todos"] += 1
                user_stats["completed_todos"] += 1
            elif todo["userId"] == user["id"]:
                user_stats["total_todos"] += 1

        user_stats["completion_rate"] = float(user_stats["completed_todos"] / user_stats["total_todos"])
        results.append(user_stats)

    return results

@app.get("/todos/search")
def search_todos(user_id: int = None, completed: bool = None):
    try:
        todos = requests.get("https://jsonplaceholder.typicode.com/todos")
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        parsed_users = users.json()
        parsed_todos = todos.json()
    except:
        return {"error": "an error while fetching has occurred"}

    user_names = {}
    for user in parsed_users:
        user_names[user["id"]] = user["name"]

    if user_id is not None:
        parsed_todos = [todo for todo in parsed_todos if todo["userId"] == user_id]

    if completed is not None:
        parsed_todos = [todo for todo in parsed_todos if todo["completed"] == completed]

    for todo in parsed_todos:
        todo["user_name"] = user_names[todo["userId"]]
    return parsed_todos
