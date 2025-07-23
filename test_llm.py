import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("🔐 Using API key:", api_key)

# Configure Gemini with the key
genai.configure(api_key=api_key)

# Use a known working model
model = genai.GenerativeModel("gemini-1.5-flash")

# Send a prompt to Gemini
response = model.generate_content("Write an SQL query to get products with ROAS > 2.0.")
print("🧠 Gemini Response:\n", response.text)
