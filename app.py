from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to this webpage!, This webpage has been viewed a number of time(s)"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)