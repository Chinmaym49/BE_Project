from flask import Flask, session, request, redirect, render_template, url_for, flash, jsonify
import mysql.connector
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "cD7nTw3jF4cwA1dv"
app.permanent_session_lifetime = timedelta(days=10)

conf={"host":"remotemysql.com","user":"xjkizVz0D6","password":"cQDyeM6Uxx","database":"xjkizVz0D6"}
tags=[]

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route("/askQuestion", methods=["GET", "POST"])
def askQuestion():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
    return render_template('ask.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/questions", methods=["GET", "POST"])
def questions():
    return "Questions"

@app.route("/profile", methods=["GET", "POST"])
def profile():
    return "Profile"

@app.route("/tags")
def tagpage():
    global tags
    if len(tags)==0:
        db=mysql.connector.connect(**conf)
        cur=db.cursor()
        cur.execute("select * from Tag")
        tags=cur.fetchall()
        cur.close()
    return render_template("tags.html",tags=tags,n=len(tags))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")




