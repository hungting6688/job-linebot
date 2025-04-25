from gpt_summarizer import summarize_jobs
import json

def get_jobs():
    return [
        "台灣大哥大 徵數據分析師，月薪 60,000 元，需出差",
        "聯發科 徵海外業務專員，需商務英文，Asia market 經驗",
        "X公司招募 AI 工程師，薪資 negotiable，可 remote"
    ]

def generate_daily_report(user_id):
    jobs = get_jobs()
    summary = summarize_jobs(jobs)
    return f"📢 今日推薦職缺：\n" + "\n".join(jobs) + "\n---\n🤖 GPT 分析摘要：\n" + summary

def generate_weekly_summary(user_id):
    return "📊 本週推薦總結功能開發中..."
