import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load Gemini API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to send prompt to Gemini
def get_sql_from_question(question: str, schema_hint: str = "") -> str:
    prompt = f"""
You are an AI assistant for a retail e-commerce database. Your job is to convert natural language questions into SQL queries.

Database schema:
{schema_hint}

Question: {question}
Convert this question into an SQL query.
Only return the SQL query, nothing else.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
