import sqlite3
from app.llm import get_sql_from_question

DB_PATH = "ecommerce.db"

SCHEMA_HINT = """
Tables:
- ad_metrics(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
- total_sales(item_id, total_sales)
- eligibility(eligibility_datetime_utc, item_id, eligibility, message)
"""

def answer_question(question: str) -> dict:
    try:
        # Step 1: Generate SQL using Gemini
        sql = get_sql_from_question(question, schema_hint=SCHEMA_HINT)

        # Step 2: Clean up any markdown formatting
        sql = sql.strip().replace("```sql", "").replace("```", "").strip()
        print("✅ Clean SQL:", sql)

        # Step 3: Execute the SQL query
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        # Step 4: Extract one-word answer
        result = [dict(zip(columns, row)) for row in rows]
        if result and len(result) > 0:
            first_value = list(result[0].values())[0]
            return {"answer": str(first_value)}
        else:
            return {"answer": "None"}

    except Exception as e:
        return {"error": str(e)}
