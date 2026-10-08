import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat_history = []

print("🤖 AI Chatbot is ready!")
print("Type 'exit' to quit.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Goodbye! 👋")
        break

    chat_history.append(f"User: {user_message}")

    conversation = "\n".join(chat_history)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=conversation
    )

    print("AI:", response.text)

    chat_history.append(f"AI: {response.text}")