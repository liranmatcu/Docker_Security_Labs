from flask import send_file, request, Flask

app = Flask(__name__)

@app.route('/get_image')
def get_image():

    print(request.args.get("name"))

    return send_file('static/tcu.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)