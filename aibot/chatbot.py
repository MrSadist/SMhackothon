import google.generativeai as genai
import os

# Siz taqdim etgan API kaliti
API_KEY = "AIzaSyCJHk6kZeiFezHfb3Qcxw39QW30KnqLcMU"

# genai kutubxonasini sozlash
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def ask_gemeni(question):
    try:
        response=model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"