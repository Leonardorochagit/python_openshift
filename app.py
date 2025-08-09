from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá Leonardo! 🚀 Seu app Python no OpenShift está rodando!"

if __name__ == "__main__":
    # O OpenShift espera que a app rode na porta 8080
    app.run(host="0.0.0.0", port=8080)
