import json, os
def load_user_config(user_id):
    try:
        with open("user_config.json", "r") as f:
            data = json.load(f)
        return data.get(user_id, {"location": "台北", "salary": "50000+"})
    except:
        return {"location": "台北", "salary": "50000+"}

def save_user_config(user_id, config):
    try:
        with open("user_config.json", "r") as f:
            data = json.load(f)
    except:
        data = {}
    data[user_id] = config
    with open("user_config.json", "w") as f:
        json.dump(data, f)

def save_history(user_id, jobs, summary):
    record = {"user_id": user_id, "jobs": jobs, "summary": summary}
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(record)
    with open("history.json", "w") as f:
        json.dump(data, f, indent=2)
