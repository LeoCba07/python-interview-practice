import requests

def safe_fetch_user(user_id: int) -> dict:
    # Fetch a single user by ID
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    try:
        data = requests.get(url)
        if data.status_code != 200:
            return {"error": True, "message": "User not found"}
        parsed_data = data.json()
    except:
        return {"error": True, "message": "Network error"}
    # Handle:
    #   - User not found (404)
    #   - Network error
    #   - Invalid JSON
    # Return the user dict on success, or an error dict on failure
    return parsed_data

# Tests
print(safe_fetch_user(1))    # Should return user data
print(safe_fetch_user(999))  # Should return error dict (not found)

# Expected success:
# {"id": 1, "name": "Leanne Graham", ...}

# Expected failure:
# {"error": True, "message": "User not found"}
