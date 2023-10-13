from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sanket")
def harry():
    return "Hello sanket bhai4!"

app.run(debug=True)