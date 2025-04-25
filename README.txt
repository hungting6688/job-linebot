【Render 雲端部署教學】

1️⃣ 建立 GitHub Repository，將本資料夾所有內容上傳（含 config.yaml）

2️⃣ 前往 https://render.com，註冊或登入

3️⃣ 點選 New → Web Service → 連接你的 GitHub → 選擇此 repo

4️⃣ 部署設定：
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py
   - Environment: Python 3
   - Plan: Free

5️⃣ 部署完成後，Render 會給你一組 URL，例如：https://your-bot.onrender.com

6️⃣ 前往 LINE Developers → Messaging API → Webhook URL 改成：
   https://your-bot.onrender.com/callback

7️⃣ 點「Verify」成功後即可運作！

🧪 測試用語：
- 「啟動職缺搜尋」
- 「暫停職缺搜尋」
- 「狀態」
