from flask import Flask, render_template, request, jsonify
from bot import load_rulesfile, find_user_intent, get_user_response

app = Flask(__name__)

rules = load_rulesfile()  # Load rules.json

# In-memory chat history (clears when server stops)
chat_history = []

@app.route("/")
def home():
    return render_template("index.html", chat_history=chat_history)

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("user_input", "")
    intent = find_user_intent(user_text, rules)
    bot_reply = get_user_response(intent, rules)

    # Add to in-memory history
    chat_history.append({"user": user_text, "bot": bot_reply})

    # Return JSON
    return jsonify({"user": user_text, "bot": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
