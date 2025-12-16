import requests

def get_user_completion_stats(users_url: str, todos_url: str) -> list[dict]:
    # 1. Fetch users and todos
    users_raw_data = requests.get(users_url)
    todos_raw_data = requests.get(todos_url)
    parsed_users = users_raw_data.json()
    parsed_todos = todos_raw_data.json()
    # 2. For each user, calculate how many todos they completed vs total
    completion_stats = []
    for user in parsed_users:
        user_completion_stats = {"name": user["name"],
                                 "completed": 0,
                                 "total": 0,
                                 "rate": 0
        }
        for todo in parsed_todos:
            if user["id"] == todo["userId"] and todo["completed"]:
                user_completion_stats["completed"] += 1
                user_completion_stats["total"] += 1
            elif user["id"] == todo["userId"]:
                user_completion_stats["total"] += 1
        user_completion_stats["rate"] = float(user_completion_stats["completed"] / user_completion_stats["total"])
        completion_stats.append(user_completion_stats)

    sorted_list = sorted(completion_stats, key=lambda d: d["rate"], reverse=True)
    return sorted_list
    # 3. Return a list of dicts sorted by completion rate (highest first)

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"
print(get_user_completion_stats(users_url, todos_url))

# Expected shape:
# [
#     {"name": "Leanne Graham", "completed": 11, "total": 20, "rate": 0.55},
#     {"name": "Ervin Howell", "completed": 8, "total": 20, "rate": 0.4},
#     ...
# ]
