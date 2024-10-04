import json
import requests
from collections import Counter
from dateutil.parser import parse
from typing import List, Dict, Optional


# JSON Handling
def deserialize_json(serialized_str: str) -> Dict:
    """Deserialize a JSON string into a Python dictionary."""
    return json.loads(serialized_str)

def get_publication_year(data: Dict) -> int:
    """Extract publication year from deserialized JSON data."""
    return data["publicationYear"]

def check_topic_in_json(data: Dict, topic: str) -> bool:
    """Check if a specific topic is present in the deserialized JSON data."""
    return topic in data.get("topics", [])


# GitHub API Handling
def fetch_github_repos(username: str) -> List[Dict]:
    """Fetch the GitHub repositories of a user using the GitHub API."""
    endpoint = f"https://api.github.com/users/{username}/repos"
    response = requests.get(endpoint)
    response.raise_for_status()  # Ensure we handle bad responses
    return response.json()

def extract_repo_creation_dates(repos: List[Dict]) -> List:
    """Extract creation dates from the list of repository data."""
    return [parse(repo["created_at"]) for repo in repos]

def count_repos_by_month(dates: List) -> Counter:
    """Count the number of repositories created by month."""
    return Counter(date.month for date in dates)

def count_repos_by_weekday(dates: List) -> Counter:
    """Count the number of repositories created by weekday."""
    return Counter(date.weekday() for date in dates)

def get_last_5_repo_languages(repos: List[Dict]) -> List[Optional[str]]:
    """Get the programming languages of the last 5 repositories."""
    last_5_repositories = sorted(repos, key=lambda r: r["pushed_at"], reverse=True)[:5]
    return [repo["language"] for repo in last_5_repositories]




