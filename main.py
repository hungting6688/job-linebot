from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os, json

from job_searcher import generate_daily_report, generate_weekly_summary

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

app = Flask(__name__)

def load_user_config(user_id):
    try:
        with open("user_config.json", "r") as f:
            data = json.load(f)
        return data.get(user_id, {"location": "台北", "salary": "50000+"})
    except:
        return {"location": "台北", "salary": "50000+"}

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text.strip().lower()
    user_id = event.source.user_id

    if msg == "/今日推薦":
        reply = generate_daily_report(user_id)
    elif msg in ["/週報", "/本週總結"]:
        reply = generate_weekly_summary(user_id)
    elif msg == "/我的紀錄":
        user_cfg = load_user_config(user_id)
        reply = f"📌 你的條件紀錄：\n地區：{user_cfg['location']}\n薪資：{user_cfg['salary']}"
    else:
        reply = f"✅ 我收到你的訊息了：{msg}"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
