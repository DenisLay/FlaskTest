from flask import Flask

app = Flask('Name')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"