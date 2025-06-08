from flask import Flask, request, render_template
from chatbot import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["message"]
        bot_reply = get_response(user_input)
    return render_template("index.html", reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)
