import streamlit as st
st.text(open(".streamlit/secrets.toml").read())

from utils import query_gemini
import re
API = st.secrets.get("GEMINI_API_KEY")
if not API:
    st.error("⚠️ GEMINI_API_KEY not found! Please check your .streamlit/secrets.toml file.")
    st.stop()

def clean_html(raw_text):
    return re.sub(r"<[^>]+>", "", raw_text).strip()

st.set_page_config(page_title="MoodMatch", layout="centered")

# Custom Styles
st.markdown("""
<style>
    html, body { background-color: #f6f0fa; font-family: 'Georgia', serif; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .title-text { font-size: 3em; text-align: center; color: #7b2cbf; margin-bottom: 0.5em; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title-text'>🧠 MOODMATCH 💗</div>", unsafe_allow_html=True)
st.divider()

st.markdown("### What would you like MoodMatch to generate?")
content_type = st.radio("Select content type:", ["Quote", "Poem", "Story", "Caption", "Song"])

st.markdown("### Answer a few questions to help us understand your emotional vibe")

q1 = st.selectbox("1. How was your day? 🌞", [
    "Tiring and dull", "Energetic and bright", "Full of worries",
    "Peaceful and relaxing", "Emotionally overwhelming",
    "Chaotic and unpredictable", "Mentally drained", "Heartwarming and cheerful"
])
q2 = st.selectbox("2. What do you feel like doing right now?", [
    "Lying down and thinking", "Going for a walk or run", "Talking to a friend",
    "Journaling or reading", "Dancing or watching a movie",
    "Listening to music alone", "Browsing social media aimlessly"
])
q3 = st.selectbox("3. Pick the word that matches your vibe 🫶", [
    "Melancholy", "Inspired", "Restless", "Calm", "Excited",
    "Frustrated", "Vulnerable", "Horny"
])

if st.button("✨ Generate Response ✨"):
    mood_summary = f"Day: {q1}. Current desire: {q2}. Emotional vibe: {q3}."
    prompt = f"Generate a {content_type.lower()} that reflects the following mood: {mood_summary}"
    
    with st.spinner("Loading the response..."):
        result = query_gemini(prompt, API)
        result = clean_html(result)

    st.subheader(f"📝 Your {content_type}")
    st.markdown(
        f"<div style='background-color:#fdfaf1; padding:20px; border-radius:12px; font-size:18px; line-height:1.75; white-space:pre-wrap;'>{result}</div>",
        unsafe_allow_html=True
    )





