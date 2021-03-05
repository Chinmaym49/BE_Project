from flask import Flask, session, request, redirect, render_template, url_for, flash, jsonify
import mysql.connector
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "cD7nTw3jF4cwA1dv"
app.permanent_session_lifetime = timedelta(days=10)

db = mysql.connector.connect(
    host="remotemysql.com", user="xjkizVz0D6", password="cQDyeM6Uxx", database="xjkizVz0D6")


@app.route("/")
def homepage():
    return "-_-"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
