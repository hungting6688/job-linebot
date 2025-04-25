import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_jobs(job_list):
    job_text = "\n".join([f"{i+1}. {job}" for i, job in enumerate(job_list)])
    prompt = f"請根據以下職缺內容，摘要出推薦原因與亮點：\n{job_text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT 摘要失敗：{str(e)}"
