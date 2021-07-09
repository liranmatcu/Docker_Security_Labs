from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def tcu():
    if request.method == "POST":

        return redirect("http://d2l.tcu.edu")

    return render_template("site_a.html")


@app.route('/site_a', methods=["GET", "POST"])
def site_a():
    return render_template("site_a.html")


@app.route('/site_b', methods=["GET", "POST"])
def site_a():
    return render_template("site_a.html")


@app.route('/site_b', methods=["GET", "POST"])
def site_a():
    return render_template("site_b.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")
