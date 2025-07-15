from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = '7460080838:AAGkMHTE11sNb-cqrKKRKKs9V9J6ZTVjxms'
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
DEFAULT_CHAT_ID = '6896590701'

@app.route('/send-text', methods=['POST'])
def send_text():
    data = request.json
    chat_id = data.get("chat_id", DEFAULT_CHAT_ID)
    message = data.get("message", "No message provided")

    res = requests.post(f"{TELEGRAM_API}/sendMessage", json={
        "chat_id": chat_id,
        "text": message
    })
    return jsonify(res.json())

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        print(f"Received from {chat_id}: {text}")

        # Optional auto-reply
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": f"You said: {text}"
        })
    except Exception as e:
        print("Error:", e)

    return jsonify({"ok": True})

@app.route('/')
def home():
    return "MCP Telegram Server is running!"

if __name__ == '__main__':
    app.run()
