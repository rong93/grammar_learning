import os

from flask import Flask, send_from_directory

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")


if __name__ == "__main__":
    # 用環境變數的埠號開網頁。
    # port = 7860
    port = int(os.environ.get("PORT", "7860"))
    app.run(host="0.0.0.0", port=port)
