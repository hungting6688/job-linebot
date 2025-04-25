# main.py 內容省略（佔位）
from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
