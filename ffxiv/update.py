import json
import requests
import time
from urllib.parse import urlparse

def update_time():
    with open('ffxiv/dalamudrepo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    current_timestamp = int(time.time())

    for plugin in data:
        plugin["LastUpdate"] = current_timestamp

    with open('ffxiv/dalamudrepo.json', 'w', encoding='utf-8') as f:
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
    with open('ffxiv/dalamudrepo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for plugin in data:
        repoUrl = plugin["RepoUrl"]
        parsed_url = urlparse(repoUrl)
        path = parsed_url.path
        last_part = path.split('/')[-1]
        plugin["DownloadCount"] = get_download_count(repo_owner, last_part)

    with open('ffxiv/dalamudrepo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def reorder_json():
    with open('ffxiv/dalamudrepo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    key_order = [
    "Author", "Name", "InternalName", "DalamudApiLevel", "Punchline", "Description",
    "Tags", "CategoryTags", "RepoUrl", "IconUrl", "AssemblyVersion", "ApplicableVersion", "IsHide", 
    "IsTestingExclusive", "DownloadCount", "DownloadLinkInstall", 
    "DownloadLinkTesting", "DownloadLinkUpdate", "LastUpdate"
    ]
    for entry in data:
        entry_reordered = {key: entry[key] for key in key_order if key in entry}
        entry.clear()
        entry.update(entry_reordered)
    with open('ffxiv/dalamudrepo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


update_time()
update_download_count("KirisameVanilla")
reorder_json()