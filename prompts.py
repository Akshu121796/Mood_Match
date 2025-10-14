def get_mood_questions():
    return [
        "How are you feeling right now?",
        "What's your energy level like today?",
        "Any specific event that impacted your mood recently?"
    ]

def generate_prompt(mood, category):
    return f"Generate a {category} that reflects the mood: {mood}."
