import requests

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"[CONTAINER SUCCESS] User: {data['login']} | Repos: {data['public_repos']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    fetch_github_profile("benitaadakeja")