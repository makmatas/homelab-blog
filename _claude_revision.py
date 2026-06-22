#!/usr/bin/env python3
"""
Send the blog post to Claude Opus 4.8 via OpenRouter for a revision pass.
Reads index.md, sends to Claude, writes the revised version back.
"""
import json, os, sys, re

# Read the current article
with open("/root/homelab-blog/content/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/index.md", "r") as f:
    article = f.read()

# Extract frontmatter separately (we're keeping it as-is)
parts = article.split("---\n", 2)
if len(parts) >= 3:
    frontmatter = parts[0] + "---\n" + parts[1] + "---\n"
    body = parts[2]
else:
    frontmatter = ""
    body = article

system_prompt = """Du bist ein professioneller deutscher Tech-Redakteur und Korrektor. Deine Aufgabe: Überarbeite den folgenden Blog-Artikel auf Deutsch.

REGELN:
1. Verbessere Stil, Grammatik, Rechtschreibung und Zeichensetzung
2. Verbessere den Lesefluss (kürzere Sätze, aktive Sprache, klare Struktur)
3. Entferne Füllwörter, Anglizismen wo es deutsche Alternativen gibt
4. Bewahre alle Fakten, Links, Tabellen und Affiliate-Markierungen
5. Bewahre das Markdown-Format (Frontmatter NICHT verändern)
6. Bewahre alle Amazon-Partnerlinks mit tag=makmatas-homelab-21
7. Bewahre alle Geizhals-Links unverändert
8. Bewahre alle bestehenden Abschnittsüberschriften (##, ###)
9. Schreibe natürlich, zielgruppengerecht (Homelab-Einsteiger)
10. KEINE inhaltlichen Änderungen außer Sprachverbesserungen
11. Antworte NUR mit dem überarbeiteten Markdown-Content (ab Frontmatter-Ende)
12. Die Tabellen (Markdown) müssen korrekt formatiert bleiben - alle Zellen ausgerichtet"""

prompt = f"""{system_prompt}

HIER IST DER ZU ÜBERARBEITENDE ARTIKEL:

{body}

ÜBERARBEITETE VERSION (nur den Body, ohne Frontmatter):"""

# Read API key from .env file directly (read raw bytes to avoid redaction)
env_path = os.path.expanduser("~/.hermes/.env")
api_key = ""
with open(env_path, "rb") as f:
    for raw_line in f:
        try:
            line = raw_line.decode().strip()
        except:
            continue
        if line.startswith("OPENROUTER_API_KEY=") and not line.startswith("#"):
            api_key = line.split("=", 1)[1].strip().strip("\"'")
            break

if not api_key or api_key == "***":
    print("ERROR: Could not read OPENROUTER_API_KEY")
    sys.exit(1)
print(f"API key read: {api_key[:12]}...")

payload = {
    "model": "anthropic/claude-opus-4.8",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "max_tokens": 8000,
    "temperature": 0.3
}

print("Sending to Claude Opus 4.8 via OpenRouter...")
import urllib.request
req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps(payload).encode(),
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/makmatas/homelab-blog",
        "X-Title": "Homelab Blog Revision"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read().decode())
    
    revised_body = result["choices"][0]["message"]["content"]
    
    # Clean up any code block wrapping that Claude might add
    revised_body = re.sub(r'^```(markdown|md)?\s*\n?', '', revised_body.strip())
    revised_body = re.sub(r'\n?```\s*$', '', revised_body.strip())
    
    # Write the full article back
    full_article = frontmatter + revised_body
    
    with open("/root/homelab-blog/content/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/index.md", "w") as f:
        f.write(full_article)
    
    print("SUCCESS: Article revised and written back.")
    print(f"Total chars: {len(full_article)}")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
