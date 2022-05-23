from flask import Flask, request

app = Flask(__name__)

@app.route("/one", methods = ["GET"])
def one():
    return "one"

@app.route("/two", methods = ["POST"])
def two():
    if request.methods == 'POST':
        return "two"
    return "temp"

@app.route("/three", methods = ["GET"])
def three():
    return "three"

@app.route("/four", methods = ["POST"])
def four():
    if request.methods == 'POST':
        return "four"
    return "temp"

@app.route("/five", methods = ["GET"])
def five():
    return "five"

@app.route("/six", methods = ["POST"])
def six():
    if request.methods == 'POST':
        return "six"
    return "temp"

@app.route("/seven", methods = ["GET"])
def seven():
    return "seven"

@app.route("/eight", methods = ["POST"])
def eight():
    if request.methods == 'POST':
        return "eight"
    return "temp"

@app.route("/nine", methods = ["GET"])
def nine():
    return "nine"

@app.route("/ten", methods = ["POST"])
def ten():
    if request.methods == 'POST':
        return "ten"
    return "temp"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)