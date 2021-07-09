from flask import Flask, make_response, render_template, request, redirect

from datetime import datetime, timedelta
import time
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(import_name=__name__,
            static_folder='static')

# app = Flask(__name__)

class Config(object):  # change password and database here
    SQLALCHEMY_DATABASE_URI = 'mysql://root:<password>@127.0.0.1:3306/Cookies_DB'
    '''
    Postgres:
    postgresql://user:password@localhost/mydatabase

    MySQL:
    mysql://user:password@localhost/mydatabase

    Oracle:
    oracle://user:password@127.0.0.1:1521/sidname

    SQLite:
    sqlite:////absolute/path/to/foo.db
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Whether data changes are tracked in Flask
    SQLALCHEMY_ECHO = False  # Displays the generated SQL statements

app.config.from_object(Config)  # Import the configuration into the project

db = SQLAlchemy(app)

# Initialized database
def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    db = SQLAlchemy()
    db.init_app(app)
    return app

# ck_table
class ck_table(db.Model):
    __tablename__ = 'ck_table'
    id = db.Column('id', db.Integer, primary_key=True, doc='Auto_ID')
    cookiekey = db.Column(db.String(32), doc='cookiekey')  # key of cookie, userID
    value = db.Column(db.String(32), doc='value')  # value of cookie
    referer = db.Column(db.String(50), doc='referer')
    cookietype = db.Column(db.String(10), doc='cookietype')
    visittime = db.Column(db.DATE, doc='DATE')
    usragent = db.Column(db.String(150), doc='usragent')

@app.route("/")
def homepage():
    img_path = './static/best-cookie.jpg'
    img_stream = return_img_stream(img_path)
    
    receivedck = request.cookies.get('userID')  # 获取cookie
    referer = request.headers.get('Referer')
    usragent = request.headers.get('User-Agent')
    if receivedck is None or ck_table.query.filter_by(value=receivedck).first() is None:  # 新建cookie
        idbytime = str(int(time.time()))
        expiretime = 'Sun, 24-Apr-2022 23:19:28 GMT'  # 格林尼治时间，要减8个小时;在新版本的http协议中，expires参数被废弃
        maxage = '31536000'  # max_age优先级高于Expires, 但IE8以下的浏览器不支持
        # set-cookie
        # resp = make_response('Your cookie is properly set as ' + idbytime + ' !')
        resp = make_response(render_template('cookie.html',img_stream=img_stream))
        resp.set_cookie(key='userID', value=idbytime, expires=expiretime, max_age=maxage, path='/', samesite='None', secure=True)
        # 写入数据库
        newUser = ck_table(cookiekey='userID', value=idbytime, referer=referer, cookietype='set', visittime=datetime.now(), usragent=usragent)
    else: # 记录访问
        newUser = ck_table(cookiekey='userID', value=receivedck, referer=referer, cookietype='return', visittime=datetime.now(), usragent=usragent)
        # resp = make_response('Your cookie ' + receivedck + ' is properly received!')
        resp = make_response(render_template('cookie.html',img_stream=img_stream))
    db.session.add(newUser)
    db.session.commit()
    return resp


# Original code
@app.route('/site_a', methods=["GET", "POST"])
def site_a():
    if request.method == "POST":

        return redirect("http://d2l.tcu.edu")

    return render_template("site_a.html")

# @app.route('/site_a', methods=["GET", "POST"])
# def site_a():
#     return render_template("site_a.html")


@app.route('/site_b', methods=["GET", "POST"])
def site_a():
    return render_template("site_a.html")


@app.route('/site_b', methods=["GET", "POST"])
def site_a():
    return render_template("site_b.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")
    app.run(debug=True)
