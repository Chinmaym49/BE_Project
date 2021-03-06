from flask import Flask, session, request, redirect, render_template, url_for, flash, jsonify
import mysql.connector
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "cD7nTw3jF4cwA1dv"
app.permanent_session_lifetime = timedelta(days=10)

conf = {"host": "remotemysql.com", "user": "xjkizVz0D6",
        "password": "cQDyeM6Uxx", "database": "xjkizVz0D6"}
tags = []


@app.route("/register")
def register():
    ''' db = mysql.connector.connect(**conf)
    mycursor = db.cursor()

    sql = "INSERT INTO User (id, handle, email, password) VALUES (%s, %s, %s, %s)"
    val = ("1", "Cap", "shaileshborate@gmail.com", "12345678")
    mycursor.execute(sql, val)

    db.commit()

    print(mycursor.rowcount, "record inserted.")
    '''
    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        db = mysql.connector.connect(**conf)
        cur = db.cursor()

        cur.execute(
            'SELECT * FROM User WHERE email = %s AND password = %s', (email, password))
        account = cur.fetchone()
        print(account)
        if account:
            session['id'] = account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            print(msg)
            return render_template('index.html', session=session)
        else:
            print(msg)
            msg = 'Incorrect username / password !'
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/askQuestion", methods=["GET", "POST"])
def askQuestion():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
    return render_template('ask.html', session=session)


@app.route("/questions", methods=["GET", "POST"])
def questions():
    return "Questions"


@app.route("/profile", methods=["GET", "POST"])
def profile():
    return session['username']


@app.route("/tags/<int:page_no>")
def tagpage(page_no):
    global tags
    if len(tags) == 0:
        db = mysql.connector.connect(**conf)
        cur = db.cursor()
        cur.execute("select * from Tag")
        tags = cur.fetchall()
        cur.close()
    start = (page_no-1)*16
    end = min(len(tags), page_no*16)
    return render_template("tags.html", tags=tags, start=start, end=end, page_no=page_no)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
