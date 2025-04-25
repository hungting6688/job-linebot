import datetime
import random

def fetch_daily_jobs():
    sample_jobs = [
        {"title": "Business Developer - Asia Market", "location": "Amsterdam", "note": "mandarin is a plus"},
        {"title": "Sales Manager (Taiwan)", "location": "Taipei", "salary": 60000, "note": "需出差"},
        {"title": "Marketing Executive", "location": "Berlin", "note": "Asia expansion"},
        {"title": "Account Manager", "location": "Kaohsiung", "salary": 48000, "note": "需出差"}
    ]

    results = []
    for job in sample_jobs:
        score = random.randint(60, 95)
        job["score"] = score
        if score > 85:
            job["highlight"] = "🔥 最看好職缺"
        results.append(job)

    return results

def generate_daily_report():
    jobs = fetch_daily_jobs()
    today = datetime.date.today().isoformat()
    message = f"📌 {today} 推薦職缺報告：\n\n"
    for job in jobs:
        line = f"- {job['title']}（{job['location']}）\n  推薦分數：{job['score']} 分"
        if 'highlight' in job:
            line += f" {job['highlight']}"
        line += "\n"
        message += line + "\n"
    return message

def generate_weekly_summary():
    return "📊 本週職缺推薦週報：\n\n" + generate_daily_report()
