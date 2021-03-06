from flask import Flask, session, request, redirect, render_template, url_for, flash, jsonify
import mysql.connector, math
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "cD7nTw3jF4cwA1dv"
app.permanent_session_lifetime = timedelta(days=10)

conf={"host":"remotemysql.com","user":"xjkizVz0D6","password":"cQDyeM6Uxx","database":"xjkizVz0D6"}
tags=[]
rendered_tags=[]
search_string = ""

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
    db=mysql.connector.connect(**conf)
    cur=db.cursor()
    query="select Question.id,Question.title from Question"
    cur.execute(query)
    ques=cur.fetchall()
    cur.close()
    tags=[]
    anscnt=[]
    users=[]
    for id,title in ques:
        cur=db.cursor()
        query="select Tag.tag from Question,Tag,QuesTag where Question.id=QuesTag.qid,QuesTag.tid=Tag.id,Question.id=?".format(id)
        cur.execute(query)
        tgs=cur.fetchall()
        cur.close()
        tags.append([t for t in tgs])

        query="select count(*) from Question,QuesAns,Answer where Question.id=QuesAns.qid,QuesAns.aid=Answer.id,Question.id=?".format(id)
        cur.execute(query)
        c=cur.fetchall()
        cur.close()
        anscnt.append(c[0][0])

        query="select Question.uid,User.handle from Question,User where Question.id=?,Question.uid=User.id".format(id)
        cur.execute(query)
        u=cur.fetchall()
        cur.close()
        users.append(u)

    return render_template("questions.html",ques=ques,n=len(ques),tags=tags,anscnt=anscnt,users=users,f=1)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    return session['username']


@app.route("/tags/<int:page_no>", methods=["GET", "POST"])
def tagpage(page_no):
    global tags
    global rendered_tags
    global search_string
    if len(tags)==0:
        db=mysql.connector.connect(**conf)
        cur=db.cursor()
        cur.execute("select * from Tag")
        tags = cur.fetchall()
        cur.close()
        rendered_tags=tags
    if request.method=="POST":
        search_string = request.form.get("tag")
        print(search_string)
        if search_string:
            rendered_tags=[]
            for tag in tags:
                if search_string in tag[1]:
                    rendered_tags.append(tag)
        else:
            rendered_tags=tags
    start=(page_no-1)*16
    end=min(len(rendered_tags),page_no*16)
    end_page=math.ceil(len(rendered_tags)/16)
    return render_template("tags.html",tags=rendered_tags,start=start,end=end,page_no=page_no,end_page=end_page,search_string=search_string,n=len(rendered_tags))

@app.route("/questions/<string:tag>")
def quespage(tag):
    pass

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
