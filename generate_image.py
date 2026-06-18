#!/usr/bin/env python3
"""
Generate featured image for blog articles via Gemini 3 Pro Image Preview (OpenRouter).
Usage: python3 generate_image.py "prompt" /path/to/output.jpg
"""
import json, urllib.request, urllib.error, sys, os, base64

def get_api_key():
    with open("/root/.hermes/.env") as f:
        for line in f:
            line = line.strip()
            if "OPENROUTER_API_KEY" in line and not line.startswith("#"):
                parts = line.split("=", 1)
                if len(parts) == 2:
                    return parts[1]
    return None

def generate_image(prompt, output_path):
    api_key = get_api_key()
    if not api_key or len(api_key) < 10:
        print("ERROR: No OpenRouter API key")
        return False

    print(f"Generating: {prompt[:60]}...")

    payload = {
        "model": "google/gemini-3-pro-image-preview",
        "messages": [{
            "role": "user",
            "content": [{"type": "text", "text": prompt}]
        }]
    }

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read())
            msg = result.get("choices", [{}])[0].get("message", {})

            # Images are in msg["images"] as list of {type, image_url: {url: data:...}}
            for img in msg.get("images", []):
                url = img.get("image_url", {}).get("url", "")
                if url.startswith("data:"):
                    b64 = url.split(",", 1)[1]
                    img_data = base64.b64decode(b64)
                    with open(output_path, "wb") as f:
                        f.write(img_data)
                    size = os.path.getsize(output_path)
                    print(f"OK: {output_path} ({size} bytes)")
                    return True

            print("No images in response")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()[:300]}")
    except Exception as e:
        print(f"Error: {e}")

    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_image.py 'prompt' /path/to/output.jpg")
        sys.exit(1)
    os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
    success = generate_image(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 1)
