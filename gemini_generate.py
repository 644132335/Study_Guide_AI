import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")


def getContentFromAI(text: str, img=None) -> str:
    if img:
        request = model.generate_content([img, text])
    else:
        request = model.generate_content(text)
    return request.text
