
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
if not os.getenv("GEMINI_API_KEY") and os.path.exists("env.env"):
    load_dotenv("env.env")

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def get_ai_response(question, subject):
    prompt = f"""
    You are an AI Study Buddy.

    Subject: {subject}
    Student question: {question}

    Explain in simple language.
    Use short sentences and one example.
    Keep the answer under 100 words.
    """

    try:
        response = client.models.generate_content_stream(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as error:
        yield f"Sorry, something went wrong: {error}"


def generate_quiz(subject):
    prompt = f"""
    Generate 5 multiple-choice questions about {subject}.

    For each question:
    - Give 4 options (A, B, C, D).
    - Clearly identify the correct answer.
    - Give a short explanation.

    Keep the questions suitable for college students.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as error:
        return f"Quiz generation failed: {error}"
