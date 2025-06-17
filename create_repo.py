import requests
import json
import os

# GitHub API endpoint
url = "https://api.github.com/user/repos"

# Get GitHub token from environment
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    raise ValueError("Please set the GITHUB_TOKEN environment variable")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

data = {
    "name": "ai-qa-platform",
    "description": "AI Quality Assurance Platform - A comprehensive ML Quality Assurance platform",
    "private": False,
    "auto_init": False
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Repository created successfully!")
    print(f"Repository URL: {response.json()['html_url']}")
else:
    print(f"Failed to create repository: {response.text}")
