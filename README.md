# mini_ai_chatbot

A simple AI chatbot built with **Python** and powered by the **Groq API** using the **Llama 3.3 70B Versatile** language model. The chatbot supports conversational interactions through a command-line interface and can be extended with a web interface using Flask or Streamlit.

---

## 📌 Features

- 💬 Interactive AI chatbot
- ⚡ Powered by Groq's ultra-fast inference API
- 🧠 Uses the Llama 3.3 70B Versatile model
- 🔄 Maintains conversation history
- 🛡️ Secure API key management using environment variables
- 🌐 Easily extendable to Flask or Streamlit web applications

---

## 🛠️ Technologies Used

- Python 3.10+
- Groq Python SDK
- Flask
- Flask-CORS
- python-dotenv
- Streamlit (optional)
<img width="1305" height="717" alt="Screenshot 2026-07-20 144830" src="https://github.com/user-attachments/assets/b1c211ca-7672-41f2-81f0-d1ea8aa14479" />

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/groq-ai-chatbot.git
cd groq-ai-chatbot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a file named **.env**

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

> **Important:** Never upload your API key to GitHub.

---

## ▶️ Running the Chatbot

### Command Line Version

```bash
python main.py
```

Example:

```
You: Hello
Assistant: Hi! How can I help you today?
```

---

### Flask Backend

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

Health Check:

```
http://127.0.0.1:5000/api/health
```

---

## 📡 API Endpoint

### POST `/api/chat`

Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello!"
    }
  ]
}
```

Response

```json
{
  "reply": "Hello! How can I help you today?",
  "model": "llama-3.3-70b-versatile"
}
```

---

## 📦 Required Packages

Install manually if needed:

```bash
pip install groq
pip install flask
pip install flask-cors
pip install python-dotenv
pip install streamlit
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

## 📸 Screenshots

```
<img width="1068" height="477" alt="Screenshot 2026-07-20 144930" src="https://github.com/user-attachments/assets/097a6fbf-bb68-407f-86e0-6ddc7d535a3a" />
```
<img width="930" height="822" alt="image" src="https://github.com/user-attachments/assets/f4eae4fa-dada-4d86-8df7-6f1000569c74" />
---

## 🚀 Future Improvements

- User authentication
- Chat history storage
- Dark mode UI
- Voice input
- Speech output
- Image understanding
- Multiple AI model support
- Deployment on Render or Railway

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Pravardhan**

GitHub: https://github.com/Pravardhan-21

---

⭐ If you found this project useful, don't forget to star the repository!
