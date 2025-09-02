from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def index():
    secret = os.getenv("APP_SECRET", "(no secret)")
    return f"Hello from AKS-like K8s via Argo CD! Secret={secret}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
