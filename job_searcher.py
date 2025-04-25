from gpt_summarizer import summarize_jobs
from utils import load_user_config, save_history

def fetch_jobs(user_id):
    config = load_user_config(user_id)
    jobs = [
        f"{config['location']}某大公司 徵後端工程師，薪資 {config['salary']}",
        f"{config['location']}外商企業 招聘 AI 助理，彈性遠距",
        f"{config['location']} 初創科技 徵數據分析師，Asia market，薪資 negotiable"
    ]
    return jobs

def generate_daily_report(user_id):
    jobs = fetch_jobs(user_id)
    summary = summarize_jobs(jobs)
    save_history(user_id, jobs, summary)
    return "\n".join(["📌 推薦職缺："] + jobs + ["\n🤖 GPT 分析：", summary])

def generate_weekly_summary(user_id):
    return "📊 週報功能開發中，敬請期待！"
