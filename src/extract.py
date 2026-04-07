import requests
import json
import os

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs"
    
    response = requests.get(url)
    data = response.json()

    os.makedirs("data", exist_ok=True)

    with open("data/jobs.json", "w") as f:
        json.dump(data["jobs"], f, indent=2)

    print(f"Saved {len(data['jobs'])} jobs to data/jobs.json")

if __name__ == "__main__":
    fetch_jobs()
