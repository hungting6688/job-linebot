import os
import time
import json
import schedule
from job_searcher import generate_daily_report
from linebot import LineBotApi
from utils import load_user_config

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))

def push_daily():
    try:
        with open("user_config.json", "r") as f:
            users = json.load(f)
        for user_id in users.keys():
            msg = generate_daily_report(user_id)
            line_bot_api.push_message(user_id, {"type": "text", "text": msg})
    except Exception as e:
        print("❌ 推播失敗：", e)

schedule.every().day.at("19:00").do(push_daily)


if __name__ == "__main__":
    print("✅ Scheduler 啟動中，等待每日 19:00 推播")
    while True:
        schedule.run_pending()
        time.sleep(60)
