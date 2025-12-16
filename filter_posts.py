import requests

def get_short_titles(url: str, max_length: int) -> list[str]:
    # 1. Fetch the posts
    try:
        posts = requests.get(url)
        parsed_posts = posts.json()
    except:
        print("Failed to fetch data from API")
    # 2. Return a list of titles that are shorter than max_length characters and uppercase
    short_titles = []
    for post in parsed_posts:
        if len(post["title"]) <= max_length:
            short_titles.append(post["title"].upper())

    return short_titles

url = "https://jsonplaceholder.typicode.com/posts"
print(get_short_titles(url, 30))

# Expected: list of uppercase titles under 30 chars
# Example: ['QUI EST ESSE', 'EA MOLESTIAS QUASI...', ...]
