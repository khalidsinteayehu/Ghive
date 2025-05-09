import requests

def fetch_github_user(username: str) -> dict:
    """Fetch GitHub user data from API."""
    url = f"https://api.github.com/users/{username}"
    return requests.get(url).json()

# Add more functions (e.g., fetch_repos, fetch_contributions)
