#!/bin/bash
set -e

BLOG_DIR="/root/homelab-blog"
GH_USER="makmatas"
GH_REPO="homelab-blog"
TOKEN_FILE="/root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt"

cd "$BLOG_DIR"

GH_TOKEN=$(cat "$TOKEN_FILE")

git config user.email "makmatas@users.noreply.github.com" 2>/dev/null || true
git config user.name "makmatas" 2>/dev/null || true

git remote set-url origin "https://${GH_USER}:${GH_TOKEN}@github.com/${GH_USER}/${GH_REPO}.git"

git add -A
if ! git diff --cached --quiet; then
  git commit -m "Blog Update: $(date +%Y-%m-%d_%H:%M)"
  git push origin main
  echo "OK Deployed to: https://${GH_USER}.github.io/${GH_REPO}/"
else
  echo "Nothing to commit"
fi
