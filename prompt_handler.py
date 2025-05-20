import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_task_from_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def handle_sentiment(text):
    prompt = f"Analyze the sentiment of this sentence and say if it's Positive, Neutral, or Negative: '{text}'"
    response = model.generate_content(prompt)
    print("Sentiment:", response.text.strip())

def handle_cleaning(text):
    prompt = f"Clean the following data (remove noise, correct spelling, and normalize): '{text}'"
    response = model.generate_content(prompt)
    print("Cleaned Data:", response.text.strip())
