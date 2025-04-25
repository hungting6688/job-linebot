from job_searcher import generate_daily_report, generate_weekly_summary
import datetime

def run_scheduled_task():
    now = datetime.datetime.now()
    if now.hour == 12:
        print(generate_daily_report())
    if now.weekday() == 5:  # Saturday
        print(generate_weekly_summary())

if __name__ == "__main__":
    run_scheduled_task()
