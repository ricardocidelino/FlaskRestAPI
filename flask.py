from fLask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá mundo!"


if __name__ == "__main__":
    app.run()