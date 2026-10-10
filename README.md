# 🔷 BlueChat — AI Assistant

**Your ideas. Beyond limits.**

BlueChat is a web-based AI assistant built with Python, Flask, and the Google Gemini API. It features a modern dark interface with electric-blue accents and support for Persian and English.

## ✨ Features

- 💬 AI-powered conversations with Google Gemini
- 🌐 Bilingual interface: Persian and English
- 🎨 Modern, responsive dark UI
- ⚡ Quick message sending and interactive suggestions
- 📱 Mobile-friendly design
- 🔄 New conversation interface

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini API
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/mohamadhosseinhojatian-jpg/BlueChat.git
cd BlueChat
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Keep your API key private. Never commit your `.env` file to GitHub.**

### 5. Start the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## 🔐 Security

- Store API credentials in environment variables.
- Never publish secret keys in source code or repository files.
- Keep `.env` excluded through `.gitignore`.
