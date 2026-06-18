#!/usr/bin/env python3
"""
Deploy: Claude review (optional) → Commit → Push → GitHub Actions build.
"""
import subprocess, os, sys, time

BLOG_DIR = "/root/homelab-blog"
TOKEN_PATH="/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt"
with open(TOKEN_PATH) as f:
    token = f.read().strip()

os.chdir(BLOG_DIR)

# Claude Review für neue Artikel
r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
new = [l.split()[-1] for l in r.stdout.split("\n") if l.strip() and "index.md" in l and l.startswith("??")]

if new:
    review_script = os.path.join(BLOG_DIR, "claude_review.py")
    if os.path.exists(review_script):
        print(f"Claude review: {len(new)} article(s)")
        for p in new:
            fp = os.path.join(BLOG_DIR, p)
            if os.path.exists(fp):
                subprocess.run(["python3", review_script, fp], capture_output=True, text=True)
                time.sleep(2)

# Commit & Push -> GitHub Actions baut automatisch
subprocess.run(["git", "config", "user.email", "makmatas@users.noreply.github.com"], capture_output=True)
subprocess.run(["git", "config", "user.name", "makmatas"], capture_output=True)
git_url = f"https://makmatas:{token}@github.com/makmatas/homelab-blog.git"
subprocess.run(["git", "remote", "set-url", "origin", git_url], capture_output=True)

subprocess.run(["git", "add", "-A"])
r = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)

if r.returncode != 0:
    subprocess.run(["git", "commit", "-m", "Blog Update"])
    push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    print(push.stdout[-200:] if len(push.stdout) > 200 else push.stdout)
    print("Deployed: https://makmatas.github.io/homelab-blog/")
else:
    print("Nothing to commit")
