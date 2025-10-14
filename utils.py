import requests


#GEMINI_API_KEY = "your own api key"

def query_gemini(prompt,GEMINI_API_KEY):
    """
    Sends a prompt to Gemini 1.5 Flash and returns the generated text.
    """

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": GEMINI_API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=data)

        if response.status_code == 200:
            # print(response.json()['candidates'][0]['content']['parts'][0]['text'])
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"❌ Gemini API Error ({response.status_code}): {response.text}"
    
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"




