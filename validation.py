import google.generativeai as genai
api_key = "AIzaSyB01ouUyKFz7IGzCgEnBdHnEY9QRQXPfIQ"

genai.configure(api_key=api_key)

def answer_validation(user_answer):
    model = genai.GenerativeModel("gemini-1.5-flash")
    question, answer = list(user_answer.items())[0]
    prompt = f"""
You are a smart form validator.

Your job is to determine whether the following answer is appropriate and meaningful for the given question.

Question: "{question}"
Answer: "{answer}"

If the answer is VALID and fits the question appropriately, return:
Valid

If the answer is INVALID or irrelevant, return:
Invalid! For example: [your own example answer that fits this question well]

Only return the plain text result. Do not include anything else.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

user_answer = {
    "Who is the gift for?": "lol"
}

print(answer_validation(user_answer))