---
title: Study Assistant
emoji: 📚
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
license: mit
---

# 📚 Study Assistant

An AI-powered Study Assistant built using **Google Gemini** and **Gradio** that explains complex concepts in a beginner-friendly manner using analogies, examples, and structured explanations.

---

## Features

- 🤖 Powered by Google Gemini
- 📖 Beginner-friendly explanations
- 🎓 Two teaching personalities:
  - Friendly
  - Academic
- 💡 Uses real-world analogies
- 📝 Structured responses
- 🔄 Follow-up questions to reinforce learning
- 🌐 Simple Gradio-based web interface

---

## 📸 Demo

<img width="100%" src="demo.png"/>

---

## 🖥️ Tech Stack

- Python
- Google Gemini API (`google-genai`)
- Gradio
- Python Dotenv

---

## 📂 Project Structure

```
StudyAssistant/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/StudyAssistant.git

cd StudyAssistant
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:7860
```

---

## 🧠 Personalities

### 😊 Friendly

- Beginner-friendly
- Conversational tone
- Real-world analogies
- Encouraging explanations

### Academic

- Professional teaching style
- Detailed explanations
- Formal terminology
- Structured learning approach

---

## Example

### Input

```
Explain Java
```

### Output

- Definition
- Why Java was created
- Internal Working
- Real-world Example
- Code Example
- Advantages
- Applications
- Summary
- Follow-up Question

---

## 📦 Requirements

```text
gradio
google-genai
python-dotenv
```

---

## 💻 Sample Code

```python
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
```

Generate Response

```python
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=question
)
```


## 👨‍💻 Author

**Kiran Kumar Kandula**

- GitHub: https://github.com/chinna0425/llm-chatbot-gradio

---

