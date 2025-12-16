import requests

def group_users_by_company(url: str) -> dict[str, list[str]]:
    # Fetch users from the API
    data = requests.get(url)
    users = data.json()

    # Return a dict where:
    #   - key = company name
    users_by_company = {}
    #   - value = list of usernames who work there
    for user in users:
        user_name = user["name"]
        company = user["company"]["name"]
        if company in users_by_company:
            users_by_company[company].append(user_name)
        else:
            users_by_company[company] = [user_name]

    return users_by_company

    pass

url = "https://jsonplaceholder.typicode.com/users"
print(group_users_by_company(url))

# Expected shape:
# {
#     "Romaguera-Crona": ["Bret"],
#     "Deckow-Crist": ["Antonette"],
#     ...
# }
