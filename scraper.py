import requests

APIFY_TOKEN = "YOUR_APIFY_TOKEN"

url = f"https://api.apify.com/v2/acts/apify/instagram-profile-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"

payload = {
    "usernames": ["natgeo", "nike", "techcrunch"]
}

response = requests.post(url, json=payload)
data = response.json()

for profile in data:
    print({
        "username": profile.get("username"),
        "followers": profile.get("followersCount"),
        "following": profile.get("followsCount"),
        "bio": profile.get("biography")
    })
