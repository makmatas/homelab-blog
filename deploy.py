#!/usr/bin/env python3
"""
Deploy pipeline: Claude review → Commit → Push → GitHub Actions build.
"""
import subprocess, os, sys, time

BLOG_DIR = "/root/homelab-blog"
GH_USER = "makmatas"
GH_REPO = "homelab-blog"
REVIEW_SCRIPT = os.path.join(BLOG_DIR, "claude_review.py")
TOKEN_PATH = "/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt"

with open(TOKEN_PATH) as f:
    token = f.read().strip()

# Check for new articles → Claude review
os.chdir(BLOG_DIR)
result = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True, text=True
)
new_articles = [line for line in result.stdout.split("\n") 
                if line.strip() and "index.md" in line and line.startswith("??")]

if new_articles:
    print(f"New articles found: {len(new_articles)}")
    for article in new_articles:
        path = article.split()[-1]
        full_path = os.path.join(BLOG_DIR, path)
        if os.path.exists(full_path):
            print(f"Claude review: {path}")
            r = subprocess.run(["python3", REVIEW_SCRIPT, full_path], 
                             capture_output=True, text=True)
            print(r.stdout)
            if r.returncode != 0:
                print(f"Review failed: {r.stderr[:200]}")
            time.sleep(2)
else:
    print("No new articles, skipping Claude review")

# Git setup
subprocess.run(["git", "config", "user.email", "makmatas@users.noreply.github.com"], capture_output=True)
subprocess.run(["git", "config", "user.name", "makmatas"], capture_output=True)

git_url = f"https://{GH_USER}:{token}@github.com/{GH_USER}/{GH_REPO}.git"
subprocess.run(["git", "remote", "set-url", "origin", git_url], capture_output=True)

subprocess.run(["git", "add", "-A"])
r = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)

if r.returncode != 0:
    subprocess.run(["git", "commit", "-m", "Blog Update"])
    push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    out = push.stdout[-500:] if len(push.stdout) > 500 else push.stdout
    print(out)
    print(f"Deployed: https://{GH_USER}.github.io/{GH_REPO}/")
else:
    print("Nothing to commit")
