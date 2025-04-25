import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_jobs(jobs):
    content = "\n".join(jobs)
    prompt = f"以下是今天的職缺：\n{content}\n請給我一段摘要與推薦理由。"
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT 摘要失敗：{e}"
