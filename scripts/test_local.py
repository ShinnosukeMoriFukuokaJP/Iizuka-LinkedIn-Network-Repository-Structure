import json
import os
import sys
import urllib.request
import urllib.error

HF_TOKEN = os.environ.get("HF_TOKEN", "")
MODELS   = [
    "mistralai/Mistral-7B-Instruct-v0.3",
    "google/flan-t5-base",
    "facebook/bart-large-cnn",
]


def ping_model(model, prompt):
    url     = f"https://api-inference.huggingface.co/models/{model}"
    payload = json.dumps({
        "inputs": prompt,
        "parameters": {"max_new_tokens": 128, "return_full_text": False},
    }).encode()
    req = urllib.request.Request(
        url, data=payload,
        headers={"Authorization": f"Bearer {HF_TOKEN}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"status": resp.status, "ok": True, "body": json.loads(resp.read())}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "ok": False, "body": e.read().decode()}
    except Exception as e:
        return {"status": 0, "ok": False, "body": str(e)}


def main():
    if not HF_TOKEN:
        print("❌ HF_TOKEN未設定")
        sys.exit(1)
    prompt = "What is the Chikuho region of Fukuoka famous for?"
    for model in MODELS:
        print(f"🔍 {model}")
        r    = ping_model(model, prompt)
        icon = "✅" if r["ok"] else "❌"
        print(f"   {icon} {r['status']}")
        if r["ok"]:
            body = r["body"]
            text = body[0].get("generated_text", "") if isinstance(body, list) else str(body)
            print(f"   {text[:100]}...")
        else:
            print(f"   {r['body'][:100]}")
        print()


if __name__ == "__main__":
    main()
