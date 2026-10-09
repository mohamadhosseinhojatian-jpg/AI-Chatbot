import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    chat_history.append(f"User: {user_message}")

    conversation = "\n".join(chat_history)

    

    response = None

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=conversation
            )
            break
        except Exception:
            if attempt == 2:
                return jsonify({
                    "response": "سرویس موقتاً در دسترس نیست. لطفاً دوباره تلاش کنید."
                }), 503
            time.sleep(2)

    ai_message = response.text


    chat_history.append(f"AI: {ai_message}")

    return jsonify({"response": ai_message})


if __name__ == "__main__":
    app.run(debug=False)