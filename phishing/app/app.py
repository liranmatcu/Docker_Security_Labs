from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":

        return redirect("http://d2l.tcu.edu")

    return render_template("index.html")


@app.route('/12306', methods=["GET", "POST"])
def china():

    return render_template("12306.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")
