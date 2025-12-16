import requests

def fetch_and_summarize(url: str) -> dict:
    # 1. Fetch JSON from the URL
    data = requests.get(url)
    # 2. Return a dict with:
    parsed_data = data.json()
    total_items = len(parsed_data)
    first_title = parsed_data[0]["title"]
    last_title = parsed_data[-1]["title"]
    #    - "total_items": how many items in the response
    #    - "first_title": title of the first item
    #    - "last_title": title of the last item
    return {
        "total_items": total_items,
        "first_title": first_title,
        "last_title": last_title
    }
    pass

# Test with this free API
url = "https://jsonplaceholder.typicode.com/posts"
print(fetch_and_summarize(url))

# Expected output shape:
# {
#     "total_items": 100,
#     "first_title": "sunt aut facere...",
#     "last_title": "at nam consequatur ea..."
# }
