import requests

def get_available_models(api_key):
    url = f"https://generativelanguage.googleapis.com/v1/models"
    params = {"key": api_key}
    resp = requests.get(url, params=params, timeout=15)
    if resp.status_code == 200:
        return resp.json().get("models", [])
    else:
        return None

def query_gemini(prompt, GEMINI_API_KEY, preferred_model="gemini-2.5-flash"):
    if not GEMINI_API_KEY:
        return "❌ Missing API key."

    # Step 1: fetch available models
    models = get_available_models(GEMINI_API_KEY)
    if models is None:
        return "⚠️ Could not fetch model list from Gemini API."

    # Step 2: pick a model
    model_names = [m.get("name", "") for m in models]
    # e.g. model["name"] might be "models/gemini-2.5-flash"
    full_name = None
    for m in models:
        nm = m.get("name", "")
        if preferred_model in nm:
            full_name = nm
            break
    if full_name is None:
        # fallback to first model that supports generateContent
        # (you may check metadata in m for supported methods)
        full_name = model_names[0] if model_names else None
    if full_name is None:
        return "❌ No valid model found."

    # Step 3: call generateContent
    # remove the "models/" prefix if your URL construction expects it
    model_id = full_name.split("/", 1)[-1]
    url = f"https://generativelanguage.googleapis.com/v1/models/{model_id}:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        resp = requests.post(url, headers=headers, params=params, json=data, timeout=30)
        if resp.status_code == 200:
            j = resp.json()
            try:
                return j["candidates"][0]["content"]["parts"][0].get("text", "").strip()
            except (KeyError, IndexError):
                return "⚠️ Gemini returned no text."
        else:
            return f"❌ Gemini API Error ({resp.status_code}): {resp.text}"
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
