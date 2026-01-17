import os
import requests
import zipfile
import shutil
import tempfile

def download_github_repo(repo_url: str, target_dir: str):
    os.makedirs(target_dir, exist_ok=True)

    parts = repo_url.rstrip("/").split("/")
    owner = parts[-2]
    repo = parts[-1].replace(".git", "")

    headers = {}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    # get default branch
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(api_url, headers=headers)
    if r.status_code != 200:
        raise RuntimeError("Failed to fetch repo metadata")

    branch = r.json()["default_branch"]

    zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"
    tmp_zip = tempfile.mktemp(suffix=".zip")

    r = requests.get(zip_url, stream=True, headers=headers)
    if r.status_code != 200:
        raise RuntimeError("Failed to download repo")

    with open(tmp_zip, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    with zipfile.ZipFile(tmp_zip, "r") as z:
        z.extractall(target_dir)

    os.remove(tmp_zip)


if __name__ == "__main__":
    download_github_repo(
        repo_url="https://github.com/jatin596/storage-inference",
        target_dir="/Users/Jatin/Desktop/model-repo/new_folder"
    )
