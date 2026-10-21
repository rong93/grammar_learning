import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # 用環境變數的埠號開網頁。
    # port = 7860
    port = int(os.environ.get("PORT", "7860"))
    app.run(host="0.0.0.0", port=port)
