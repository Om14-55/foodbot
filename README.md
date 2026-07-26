# 🍳 FoodBot – AI Powered Recipe Recommendation Chatbot

FoodBot is an AI-powered recipe recommendation chatbot that helps users discover recipes based on the ingredients they already have. Instead of relying on keyword matching, FoodBot uses **Vector Search** and **Google Gemini AI** to understand the user's query and recommend the most relevant recipes with ingredient quantities and cooking instructions.

---

## 🚀 Features

- 🤖 AI-powered recipe recommendations
- 🍅 Search recipes using available ingredients
- 🧠 Semantic search using vector embeddings
- 🔍 Fast recipe retrieval with AstraDB Vector Database
- 💬 Natural language responses powered by Google Gemini
- ⚡ LangChain Retrieval-Augmented Generation (RAG)
- 🌐 Interactive Flask web application
- 📱 Simple and responsive chatbot interface

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI & LLM
- Google Gemini API
- LangChain

### Vector Database
- AstraDB (DataStax)

### Embedding Model
- Hugging Face Sentence Transformers
- `all-MiniLM-L6-v2`

### Frontend
- HTML
- CSS
- JavaScript

### Other Libraries
- Pandas
- Python-dotenv

---

# 📂 Project Structure

```text
FoodBot/
│
├── app.py
├── setup.py
├── requirements.txt
├── .env
│
├── data/
│   └── updated_food.csv
│
├── foodbot/
│   ├── ingest.py
│   ├── retrival_generation.py
│   ├── data_converter.py
│   └── __init__.py
│
├── templates/
│   └── chain.html
│
├── static/
│   ├── style.css
│   └── logo.png
│
└── README.md
```

---

# ⚙️ How It Works

### Step 1 – Load Dataset

The chatbot loads a dataset containing:

- Recipe Name
- Ingredients
- Ingredient Quantity
- Cooking Instructions

---

### Step 2 – Convert Data

Each recipe is converted into LangChain `Document` objects.

Example:

```python
Document(
    page_content=instructions,
    metadata={
        "recipe_name": name,
        "ingredients": ingredients,
        "ingredient_quantity": quantity
    }
)
```

---

### Step 3 – Generate Embeddings

The embedding model

```
sentence-transformers/all-MiniLM-L6-v2
```

converts every recipe into vector embeddings.

---

### Step 4 – Store in AstraDB

The embeddings are stored inside AstraDB Vector Database for semantic search.

---

### Step 5 – User Query

Example:

```
egg onion green chilli oil
```

The user query is converted into embeddings.

---

### Step 6 – Similarity Search

AstraDB finds the most relevant recipes using vector similarity search.

---

### Step 7 – AI Response Generation

The retrieved recipes are sent to Google Gemini.

Gemini generates a natural language response containing:

- Recipe Name
- Ingredient Quantity
- Cooking Instructions

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/Om14-55/foodbot.git
```

Move into the project

```bash
cd foodbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

ASTRA_DB_API_ENDPOINT=YOUR_ASTRA_DB_ENDPOINT

ASTRA_DB_APPLICATION_TOKEN=YOUR_ASTRA_DB_APPLICATION_TOKEN

ASTRA_DB_KEYSPACE=default_keyspace
```

---

# 📥 Load Recipe Data into AstraDB

Run

```bash
python foodbot/ingest.py
```

This process:

- Reads the CSV dataset
- Converts recipes into LangChain Documents
- Generates embeddings
- Uploads vectors into AstraDB

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 💬 Example

### User Input

```
egg onion green chilli oil
```

### FoodBot Response

```
Recipe Name:
Egg Scramble

Ingredients:
• 2 Eggs
• 1 Onion
• 2 Green Chillies
• Oil

Instructions:
1. Heat the oil.
2. Add chopped onion and green chilli.
3. Pour beaten eggs into the pan.
4. Cook for 3–4 minutes.
5. Serve hot.
```

---

# 📸 Screenshots

> Add screenshots of your application here.

Example:

```
screenshots/
│
├── home.png
├── chat.png
└── response.png
```

Then include them like this:

```markdown
## Home Page

![Home](screenshots/home.png)

## Chat Interface

![Chat](screenshots/chat.png)

## Recipe Recommendation

![Response](screenshots/response.png)
```

---

# 📌 Project Status

✅ Recipe dataset preprocessing

✅ Data conversion using LangChain Documents

✅ Hugging Face embeddings

✅ AstraDB Vector Store integration

✅ Google Gemini integration

✅ LangChain RAG pipeline

✅ Flask chatbot interface

✅ Interactive web application

---

# 🚀 Future Improvements

- User authentication
- Recipe images
- Nutritional information
- Meal planning
- Favourite recipes
- Voice-based recipe search
- Multi-language support
- Docker support
- Cloud deployment
- Mobile application

---

# 👨‍💻 Author

**Rohit Shaw**

🎓 B.Tech in Computer Science & Engineering

💻 Python | Flask | LangChain | Generative AI | Machine Learning

🔗 GitHub: https://github.com/Om14-55

🔗 LinkedIn: *(Add your LinkedIn profile here)*

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates me to build more AI-powered applications.

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and contribute to this project.
