import json
import os
import pathlib
import urllib.request
import urllib.error

HF_TOKEN = os.environ.get("HF_TOKEN", "")
PROMPT   = os.environ.get("PROMPT", "Hello, introduce yourself.")
MODEL    = os.environ.get("MODEL", "mistralai/Mistral-7B-Instruct-v0.3")

API_BASE   = "https://api-inference.huggingface.co/models"
OUTPUT_DIR = pathlib.Path("outputs")


def build_payload(prompt):
    return {
        "inputs": f"<s>[INST] {prompt} [/INST]",
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.7,
            "return_full_text": False,
        },
    }


def call_hf_api(model, payload):
    url  = f"{API_BASE}/{model}"
    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(
        url, data=data,
        headers={
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type":  "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.read().decode()}"}
    except urllib.error.URLError as e:
        return {"error": f"URLError: {e.reason}"}


def extract_text(response):
    if isinstance(response, list) and response:
        return response[0].get("generated_text", str(response))
    if isinstance(response, dict):
        return response.get("generated_text", response.get("error", str(response)))
    return str(response)


def save_output(text, model, prompt):
    OUTPUT_DIR.mkdir(exist_ok=True)
    result = {"model": model, "prompt": prompt, "output": text}
    (OUTPUT_DIR / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2)
    )
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        safe = text.replace("\n", " ").replace("\r", "")[:500]
        with open(github_output, "a") as f:
            f.write(f"result={safe}\n")
    return result


def main():
    if not HF_TOKEN:
        raise EnvironmentError("HF_TOKEN が未設定です")
    print(f"🤖 Model : {MODEL}")
    print(f"📝 Prompt: {PROMPT[:80]}...")
    response = call_hf_api(MODEL, build_payload(PROMPT))
    text     = extract_text(response)
    result   = save_output(text, MODEL, PROMPT)
    print("\n── Output ──")
    print(result["output"])


if __name__ == "__main__":
    main()
