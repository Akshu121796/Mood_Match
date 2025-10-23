# MoodMatch 🎭  

> *Your mood, your words — personalized quotes, poems, stories, and captions generated with AI.*  

MoodMatch is a **Streamlit-based GenAI app** that detects your mood through **fun, indirect multiple-choice questions** and generates **personalized creative content** (quotes, poems, short stories, or captions) using **Gemini 1.5 Flash**.  

Through **fun mood-based questions**, it interprets your emotional tone and crafts words that truly *match your mood*. 💜  

---

## ✨ Features  

- 💡 **Smart Mood Detection** — Understands your emotions from subtle cues.  
- 📝 **Personalized Content** — Generates unique pieces tailored to your vibe.  
- ⚡ **Fast & Expressive AI** — Powered by **Gemini 1.5 Flash** for instant results.  
- 🎨 **Clean Streamlit UI** — Minimal, aesthetic, and interactive.  
- 🎭 **Multi-Mode Creativity** — Choose *Quote, Poem, Story, Caption,* or *Song*.  

---

## 🧩 Tech Stack  

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **AI Model** | Google Gemini 1.5 Flash |
| **Language** | Python 3.13+ |
| **Deployment** | Streamlit Cloud / Localhost |

---

## 🚀 Getting Started  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/moodmatch.git
cd moodmatch
```

2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Add your Gemini API key
Create a folder named .streamlit in your project root and add a file secrets.toml inside it:
.toml
```
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
⚠️ If you see “GEMINI_API_KEY not found!”, verify this file path and restart Streamlit.
```

4️⃣ Run the app
```bash
streamlit run app.py
```

💬 How to Use

~Choose the content type you’d like to generate.
~Answer the three fun mood-based questions.
~Click ✨ Generate Response ✨ to let AI craft your piece.
~Enjoy your personalized quote, poem, story, caption, or song!

🪪 License

This project is licensed under the MIT License — free to use, modify, and share.
