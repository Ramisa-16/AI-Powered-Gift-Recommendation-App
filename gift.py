import google.generativeai as genai
import json

api_key = "AIzaSyB01ouUyKFz7IGzCgEnBdHnEY9QRQXPfIQ"
genai.configure(api_key=api_key)


def suggest_gift(user_answer):

    prompt = f"""
You are a smart gift recommendation assistant.

Your task is to suggest exactly **4 unique gift item names** that match the user's preferences.

**Important Rules:**
1. Suggest **three gifts** that can be from **anywhere** (independent shops, unique websites, Etsy, etc.).
2. Suggest **one additional gift** that is currently available on **Amazon**.
3. Clearly label the Amazon item as: (Amazon).
4. The gift ideas must be relevant to the user's preferences {user_answer} (occasion, interests, age, vibe, etc.).
5. All gifts should be practical, thoughtful, and ideal for a special moment—fun and comforting in nature.

Only return your response as a JSON array of strings like this:
[
  "Gift Name 1",
  "Gift Name 2",
  "Gift Name 3",
  "Gift Name 4 (Amazon)"
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


gift_ideas = suggest_gift(user_answer)
print("🎁 Suggested Gift Item Names:\n", gift_ideas)