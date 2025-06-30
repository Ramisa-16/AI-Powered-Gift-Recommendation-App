import google.generativeai as genai
import json

api_key = "AIzaSyB01ouUyKFz7IGzCgEnBdHnEY9QRQXPfIQ"
genai.configure(api_key=api_key)


def regenerate(user_answer, previous_suggestion):
    previous_text = ", ".join(previous_suggestion) if previous_suggestion else "None"

    prompt = f"""
You are a smart gift recommendation assistant.

Your task is to suggest exactly 3 unique **gift item names** that match the user's preferences{user_answer}.

Rules:
1. Suggest **three gifts** that can be from **anywhere** (independent shops, unique websites, Etsy, etc.).
2. Do NOT include any of these previously suggested items: {previous_text}.
3. The gift ideas must be relevant to the user's preferences {user_answer} (occasion, interests, age, vibe, etc.).
4. These gifts must be practical, thoughtful, and appropriate for the scenario described {user_answer}.

Only return your response as a JSON array of strings like this:
[
  "Gift Name 1",
  "Gift Name 2",
  "Gift Name 3"
]

User Preferences:
{json.dumps(user_answer, indent=2)}
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])
    json_output = response.text.strip().replace("```json", "").replace("```", "").strip()
    print("Cleaned AI Response:\n", json_output)

    try:
        parsed = json.loads(json_output)
        return json.dumps(parsed, indent=4)
    except Exception:
        return {"error": "AI response was not valid JSON."}

user_answer = {
    "Who is the gift for?": "My best friend",
    "What is the occasion?": "Her birthday",
    "What is their age (or age range)?": "25",
    "What are their main interests or hobbies?": "Music, relaxation, books",
    "What is your budget for this gift?": "$30-$60",
    "What kind of feeling should the gift give?": "Fun and comforting",
    "Do you want something for everyday use or something for a special moment?": "Special moment",
    "Do they prefer trendy or more classic gifts?": "Trendy",
    "Do they have any favorite brands, shows, or inside jokes?": "She loves Spotify, candles, and mystery novels",
    "Would you like this gift to be personalized?": "No",
    "Do you need fast shipping (like Amazon Prime)?": "Yes",
    "Is there anything else I should know to make this gift perfect?": "She just got a new apartment"
}

previous_suggestion = [
    "Personalized Passport Holder",
    "Customized Leather Travel Journal",
    "Mini Travel Jewelry Organizer",
    "Scented Candle Gift Set",
    "Bluetooth Sleep Headphones",
    "Personalized Spotify Plaque"
]

gift_ideas = regenerate(user_answer, previous_suggestion)
print("🎁 Suggested Gift Item Names:\n", gift_ideas)