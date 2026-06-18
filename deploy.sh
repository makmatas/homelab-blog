#!/bin/bash
# Deploy Script für Homelab-Blog
# Wird vom Hermes-Cronjob aufgerufen
set -e

BLOG_DIR="/root/homelab-blog"
GH_USER="makmatas"
GH_REPO="homelab-blog"
GH_TOKEN=$(cat /root/.hermes/skills/monetization/homelab-seo-blog/references/github_token.txt)

cd "$BLOG_DIR"

# Theme initialisieren falls nicht vorhanden
if [ ! -d "themes/PaperMod" ]; then
  git submodule add https://github.com/adityatelange/hugo-PaperMod themes/PaperMod 2>/dev/null || true
fi

# Neuen Artikel committen
git add -A
if git diff --cached --quiet; then
  echo "Keine Änderungen zu committen."
else
  git commit -m "Blog Update: $(date +%Y-%m-%d_%H:%M)"
fi

# Build
hugo --minify

# Remote prüfen
if ! git remote get-url origin &>/dev/null; then
  git branch -M main
  git remote add origin https://${GH_USER}:${GH_TOKEN}@github.com/${GH_USER}/${GH_REPO}.git
fi

# Pushen
git push origin main 2>&1 || {
  # Erster Push - Repo existiert noch nicht auf GitHub
  git push https://${GH_USER}:${GH_TOKEN}@github.com/${GH_USER}/${GH_REPO}.git main
}

echo "✅ Blog deployed: https://${GH_USER}.github.io/${GH_REPO}/"
