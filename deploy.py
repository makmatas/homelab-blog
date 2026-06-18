#!/usr/bin/env python3
"""Deploy new blog articles to GitHub Pages."""
import subprocess, os

BLOG_DIR = "/root/homelab-blog"
GH_USER = "makmatas"
GH_REPO = "homelab-blog"
TOKEN_PATH = "/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt"

os.chdir(BLOG_DIR)

with open(TOKEN_PATH) as f:
    token = f.read().strip()

git_url = f"https://{GH_USER}:{token}@github.com/{GH_USER}/{GH_REPO}.git"

subprocess.run(["git", "config", "user.email", "makmatas@users.noreply.github.com"], capture_output=True)
subprocess.run(["git", "config", "user.name", "makmatas"], capture_output=True)
subprocess.run(["git", "remote", "set-url", "origin", git_url], capture_output=True)

subprocess.run(["git", "add", "-A"])
r = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)
if r.returncode != 0:
    subprocess.run(["git", "commit", "-m", f"Blog Update: $(date +%Y-%m-%d_%H:%M)"])
    subprocess.run(["git", "push", "origin", "main"])
    print(f"OK Deployed: https://{GH_USER}.github.io/{GH_REPO}/")
else:
    print("Nothing to commit")
