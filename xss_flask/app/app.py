from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":

        return redirect("http://d2l.tcu.edu")

    return render_template("index.html")

@app.route('/blog', methods=["GET", "POST"])
def blog():

    endhtml = ""

    with open("/app/blog.txt", "r") as file:
        lines = file.readlines()
        for item in lines:
            endhtml += "<div class='col-12 card' style='margin-top: 10px; margin-bottom: 10px;'><div class='card-body'><p>{}</p></div></div>".format(item)

    return render_template("blog.html", blog=endhtml)


@app.route('/createblog', methods=["GET", "POST"])
def blogcreate():

    if request.method == "POST":
        content = request.form.get("content")

        #content = content.replace("<", "&lt;")
        #content = content.replace(">", "&gt;")

        with open("/app/blog.txt", "a") as file:
            file.write(content + "\n")

        return redirect("/blog")
    if request.method == "GET":
        return render_template("create.html")


@app.route('/pagenotfound', methods=["GET", "POST"])
def notfound():

    text = request.args.get("page")

    return render_template("found.html", text=text)



if __name__ == '__main__':
    app.run(host='127.0.0.1')
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")
