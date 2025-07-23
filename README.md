\# 🛍️ GenAI E-Commerce Agent



This project is an intelligent AI agent that understands natural language queries and answers them using e-commerce data via SQL. It combines Google's \*\*Gemini Pro\*\* large language model with \*\*FastAPI\*\*, \*\*SQLite\*\*, and \*\*CSV-based datasets\*\*.



---



\## 🚀 Features



\- 🤖 Natural language to SQL conversion using Gemini Pro

\- 📊 Answers business questions like:

&nbsp; - "What is the total ad sales?"

&nbsp; - "Which product had the highest ROAS?"

&nbsp; - "What is the average clicks per ad?"

\- 🗃️ Local SQLite database with 3 tables:

&nbsp; - `ad\_metrics`

&nbsp; - `total\_sales`

&nbsp; - `eligibility`

\- 📂 CSV upload + data ingestion support

\- 🔌 API endpoint (`/ask`) for question answering

\- 🧪 Unit tests included

\- 🖥️ Swagger UI available at `http://127.0.0.1:8000/docs`



---



\## 📁 Project Structure



genai-agent/

├── app/

│ ├── main.py # FastAPI app

│ ├── query\_handler.py # Handles prompt → SQL → DB → result

│ └── llm.py # Gemini API calls

├── data/

│ ├── ad\_metrics.csv

│ ├── eligibility.csv

│ └── total\_sales.csv

├── create\_db.py # Loads CSV into SQLite

├── ecommerce.db # SQLite database

├── .env # API Key (GEMINI\_API\_KEY=...)

├── test\_api.py # Manual test script

├── test\_models.py

└── README.md # ← You are here



yaml

Copy

Edit



---



\## ⚙️ Setup Instructions



\### 1. Clone the Repository



```bash

git clone https://github.com/padmajanu/genai-ecommerce-agent.git

cd genai-ecommerce-agent

2\. Install Dependencies

bash

Copy

Edit

pip install -r requirements.txt

3\. Set Gemini API Key

Create a .env file:



ini

Copy

Edit

GEMINI\_API\_KEY=your\_actual\_api\_key\_here

4\. Load Data into Database

bash

Copy

Edit

python create\_db.py

5\. Start the API Server

bash

Copy

Edit

uvicorn app.main:app --reload

Then open:



📄 http://127.0.0.1:8000/docs ← Swagger UI

📘 http://127.0.0.1:8000/redoc ← ReDoc UI



📌 Example Question

json

Copy

Edit

POST /ask

{

&nbsp; "question": "What is the total ad sales?"

}

✅ Response

json

Copy

Edit

{

&nbsp; "sql": "SELECT SUM(ad\_sales) FROM ad\_metrics;",

&nbsp; "result": \[

&nbsp;   {

&nbsp;     "SUM(ad\_sales)": 419078.21

&nbsp;   }

&nbsp; ]

}

🧪 Testing

You can test the agent manually using:



bash

Copy

Edit

python test\_api.py

👩‍💻 Built With

FastAPI



SQLite



Google Generative AI



Uvicorn



🙌 Author

Padma Janu

🔗 GitHub



📃 License

This project is licensed for academic, research, and demonstration purposes.

