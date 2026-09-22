import sys
import json
import urllib.request
from urllib.error import HTTPError, URLError


def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Python-CLI-App"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return data
    except HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
        sys.exit(1)
    except URLError as e:
        print(f"Connection Error: {e.reason}")
        sys.exit(1)


def display_activity(events):
    if not events:
        print("No recent public activity found for this user.")
        return

    print("\n--- Recent Activity ---")
    for event in events[:15]:
        repo_name = event.get("repo", {}).get("name", "unknown repo")
        event_type = event.get("type")

        if event_type == "PushEvent":
            commit_count = len(event.get("payload", {}).get("commits", []))
            print(f"- Pushed {commit_count} commit(s) to {repo_name}")
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action")
            print(f"- {action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type")
            print(f"- Created a new {ref_type} in {repo_name}")
        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action")
            print(f"- {action.capitalize()} a pull request in {repo_name}")
        else:
            clean_type = event_type.replace("Event", "")
            print(f"- Performed {clean_type} action in {repo_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <github_helenugwueze>")
        sys.exit(1)

    target_user = sys.argv[1]
    activity_data = fetch_github_activity(target_user)
    display_activity(activity_data)