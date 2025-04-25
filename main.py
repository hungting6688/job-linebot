from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# ✅ 使用你提供的 Token 與 Secret（請保密）
line_bot_api = LineBotApi('g66Y9p1FahGE6WC+Ts4uOPkkYwrbPjcc9CotOkNDoBEKkPAgD6dw6vL5Yk07YZfh4ZZNhgvaKCRA6VbF5Qfx8V1k0/7sFKMgro42Ol7sbzdVD4NAWQljqqKlmGYrd1kO9w87shDV4wZR5kOwX8jJ2AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('70970e9b83dad47b74fd7c4cb99df507')

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
    user_text = event.message.text
    reply_text = f"✅ 我收到你的訊息了：{user_text}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
