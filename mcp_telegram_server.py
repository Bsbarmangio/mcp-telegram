from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = '7460080838:AAGkMHTE11sNb-cqrKKRKKs9V9J6ZTVjxms'
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
DEFAULT_CHAT_ID = '6896590701'

@app.route('/sms-webhook', methods=['POST'])
def sms_webhook():
    from_number = request.form.get('From')
    message_body = request.form.get('Body')

    telegram_message = f"📩 SMS from {from_number}:\n{message_body}"

    requests.post(f"{TELEGRAM_API}/sendMessage", json={
        "chat_id": CHAT_ID,
        "text": telegram_message
    })

    return "OK", 200

if __name__ == '__main__':
    app.run()
