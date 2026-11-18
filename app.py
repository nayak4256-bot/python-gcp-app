from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Application running on GCP GKE!"

@app.route("/hello")
def hello():
    return "Hello GCP!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

