#!/usr/bin/env python3
"""
Claude Sonnet 4.6 Review Pipeline
Liest einen generierten SEO-Artikel, schickt ihn an Claude zur Verbesserung,
überschreibt die Datei mit der verbesserten Version.
"""
import json, urllib.request, urllib.error, sys, os, re

def get_anthropic_key():
    """Extract Anthropic API key from Hermes config."""
    with open("/root/.hermes/config.yaml") as f:
        for line in f:
            if line.strip().startswith("api_key:") and "sk-ant" in line:
                return line.split("api_key:")[1].strip()
    return None

def review_article(content):
    """Send article to Claude Sonnet 4.6 for critical review + improvement."""
    api_key = get_anthropic_key()
    if not api_key:
        print("ERROR: Could not find Anthropic API key")
        sys.exit(1)

    print(f"📤 Sending article to Claude Sonnet 4.6...")

    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 8192,
        "system": """Du bist ein deutschsprachiger SEO-Content-Redakteur und Reviewer.
Deine Aufgabe: Verbessere den folgenden SEO-Artikel. Behalte die komplette Struktur, den Inhalt und alle Amazon-Links bei.
Verbessere:
1. Rechtschreibung & Grammatik
2. Satzfluss & Lesbarkeit
3. SEO-Optimierung (Keyword-Dichte, H2/H3-Struktur)
4. Fakten-Prüfung (offensichtliche Fehler korrigieren)
5. Call-to-Actions schärfer formulieren

WICHTIG: Gib NUR den verbesserten vollständigen Artikel inkl. YAML-Frontmatter zurück. Keine Erklärungen, keine Einleitungen. 
Behalte ALLE Amazon-Links mit ?tag=makmatas-homelab-21 exakt so bei.
Behalte das Datum und alle Metadaten im Frontmatter.
Ändere keine Fakten oder Produktnamen.""",
        "messages": [{"role": "user", "content": f"Hier ist der SEO-Artikel zur Verbesserung:\n\n---\n{content}\n---\n\nBitte verbessere den Artikel und gib NUR den vollständigen verbesserten Artikel zurück."}]
    }

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode(),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read())
            for block in result.get("content", []):
                if block.get("type") == "text":
                    return block["text"]
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP {e.code}: {body[:300]}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    return None

def find_latest_article():
    """Find the most recently created article in the blog content directory."""
    blog_dir = "/root/homelab-blog/content/posts"
    if not os.path.exists(blog_dir):
        print(f"ERROR: {blog_dir} not found")
        sys.exit(1)

    # Find newest directory with index.md
    newest = None
    newest_time = 0
    for root, dirs, files in os.walk(blog_dir):
        for f in files:
            if f == "index.md":
                path = os.path.join(root, f)
                mtime = os.path.getmtime(path)
                if mtime > newest_time:
                    newest_time = mtime
                    newest = path

    if not newest:
        print("ERROR: No article found")
        sys.exit(1)

    print(f"📄 Found article: {newest}")
    return newest

def main():
    # Allow passing article path as argument, or find latest
    if len(sys.argv) > 1:
        article_path = sys.argv[1]
    else:
        article_path = find_latest_article()

    if not os.path.exists(article_path):
        print(f"ERROR: Article not found: {article_path}")
        sys.exit(1)

    # Read original
    with open(article_path) as f:
        original = f.read()

    print(f"📖 Original: {len(original)} chars")

    # Send to Claude for review
    improved = review_article(original)

    if not improved:
        print("ERROR: No response from Claude")
        sys.exit(1)

    # Clean up Claude's response - sometimes adds markdown code fences
    improved = improved.strip()
    if improved.startswith("```markdown"):
        improved = improved[11:]
    if improved.startswith("```"):
        improved = improved[3:]
    if improved.endswith("```"):
        improved = improved[:-3]
    improved = improved.strip()

    # Write improved version
    with open(article_path, "w") as f:
        f.write(improved + "\n")

    print(f"✅ Claude review complete: {len(improved)} chars")
    print(f"   +{len(improved) - len(original)} chars changed")
    print(f"   Saved to: {article_path}")

if __name__ == "__main__":
    main()
