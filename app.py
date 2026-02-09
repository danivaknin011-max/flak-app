from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask 🚀"

@app.route("/ai")
def ai():
    return "Welcome to the AI section!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
