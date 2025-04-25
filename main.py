from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

line_bot_api = LineBotApi(config["channel_access_token"])
handler = WebhookHandler(config["channel_secret"])

app = Flask(__name__)
user_status = {}

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    uid = event.source.user_id
    msg = event.message.text.strip().lower()

    if msg in ["啟動職缺搜尋", "啟動"]:
        user_status[uid] = True
        reply = "✅ 已啟動職缺搜尋通知"
    elif msg in ["暫停職缺搜尋", "暫停"]:
        user_status[uid] = False
        reply = "⏸ 已暫停職缺搜尋通知"
    elif msg in ["狀態", "我的狀態"]:
        enabled = user_status.get(uid, False)
        reply = f"🔍 目前搜尋功能：{'啟動中 ✅' if enabled else '暫停中 ⏸'}"
    else:
        reply = "請輸入：啟動職缺搜尋、暫停職缺搜尋 或 狀態"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

