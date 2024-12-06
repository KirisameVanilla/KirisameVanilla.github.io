import json
import requests
import time
from urllib.parse import urlparse

def update_time():
    with open('dalamudrepo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    current_timestamp = int(time.time())

    for plugin in data:
        plugin["LastUpdate"] = current_timestamp

    with open('dalamudrepo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_download_count(repo_owner, repo_name) -> int:
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
    response = requests.get(url)
    data = json.loads(response.text)
    total_download_count = 0
    for release in data:
        for asset in release["assets"]:
            download_count = asset["download_count"]
            total_download_count += download_count
    return total_download_count

def update_download_count(repo_owner):
    with open('dalamudrepo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for plugin in data:
        repoUrl = plugin["RepoUrl"]
        parsed_url = urlparse(repoUrl)
        path = parsed_url.path
        last_part = path.split('/')[-1]
        plugin["DownloadCount"] = get_download_count(repo_owner, last_part)

    with open('dalamudrepo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



update_time()
update_download_count("KirisameVanilla")
