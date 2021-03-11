from flask import Flask, session, request, redirect, render_template, url_for, flash, jsonify
import mysql.connector
import math
import requests
from re import sub
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "cD7nTw3jF4cwA1dv"
app.permanent_session_lifetime = timedelta(days=10)

conf = {"host": "remotemysql.com", "user": "xjkizVz0D6",
        "password": "cQDyeM6Uxx", "database": "xjkizVz0D6"}

tags = [(3001, 'c#'), (3002, 'java'), (3003, 'php'), (3004, 'javascript'), (3005, 'android'), (3006, 'jquery'), (3007, 'c++'), (3008, 'asp.net'), (3009, 'html'), (3010, '.net'), (3011, 'iphone'), (3012, 'python'), (3013, 'mysql'), (3014, 'sql'), (3015, 'objective-c'), (3016, 'ios'), (3017, 'css'), (3018, 'ruby-on-rails'), (3019, 'windows'), (3020, 'linux'), (3021, 'c'), (3022, 'wpf'), (3023, 'arrays'), (3024, 'sql-server'), (3025, 'asp.net-mvc'), (3026, 'database'), (3027, 'ajax'), (3028, 'xml'), (3029, 'ruby'), (3030, 'eclipse'), (3031, 'xcode'), (3032, 'django'), (3033, 'vb.net'), (3034, 'facebook'), (3035, 'json'), (3036, 'winforms'), (3037, 'html5'), (3038, 'homework'), (3039, 'regex'), (3040, 'asp.net-mvc-3'), (3041, 'bash'), (3042, 'performance'), (3043, 'osx'), (3044, 'forms'), (3045, 'ruby-on-rails-3'), (3046, 'string'), (3047, 'visual-studio-2010'), (3048, 'multithreading'), (3049, 'visual-studio'), (3050, 'algorithm'), (3051, 'web-services'), (3052, 'actionscript-3'), (3053, 'git'), (3054, 'excel'), (3055, 'silverlight'), (3056, 'hibernate'), (3057, 'spring'), (3058, 'apache'), (3059, 'image'), (3060, 'windows-7'), (3061, 'oracle'), (3062, 'security'), (3063, 'query'), (3064, 'wcf'), (3065, '.htaccess'), (3066, 'flash'), (3067, 'linq'), (3068, 'file'), (3069, 'cocoa-touch'), (3070, 'sqlite'), (3071, 'networking'), (3072, 'sql-server-2008'), (3073, 'ubuntu'), (3074, 'oop'), (3075, 'entity-framework'), (3076, 'ipad'), (3077, 'class'), (3078, 'google-chrome'), (3079, 'perl'), (3080, 'api'), (3081, 'codeigniter'), (3082, 'shell'), (3083, 'list'), (3084, 'wordpress'), (3085, 'jsp'), (3086, 'http'), (3087, 'iis'), (3088, 'uitableview'), (3089, 'flex'), (3090, 'jsf'), (3091, 'internet-explorer'), (3092, 'jquery-ui'), (3093, 'vba'), (3094, 'linear-algebra'), (3095, 'apache2'), (3096, 'function'), (3097, 'google-maps'), (3098, 'mvc'), (3099, 'email'), (3100, 'xaml'),
        (3101, 'design'), (3102, 'generics'), (3103, 'validation'), (3104, 'real-analysis'), (3105, 'firefox'), (3106, 'debugging'), (3107, 'tsql'), (3108, 'unix'), (3109, 'matlab'), (3110, 'cocoa'), (3111, 'postgresql'), (3112, 'sql-server-2005'), (3113, 'r'), (3114, 'date'), (3115, 'google-app-engine'), (3116, 'calculus'), (3117, 'parsing'), (3118, 'sockets'), (3119, 'visual-c++'), (3120, 'winapi'), (3121, 'command-line'), (3122, 'exception'), (3123, 'url'), (3124, 'jquery-ajax'), (3125, 'session'), (3126, 'mod-rewrite'), (3127, 'svn'), (3128, 'loops'), (3129, 'visual-studio-2008'), (3130, 'design-patterns'), (3131, 'object'), (3132, 'datetime'), (3133, 'unit-testing'), (3134, 'sharepoint'), (3135, 'c#-4.0'), (3136, 'rest'), (3137, 'data-binding'), (3138, 'sorting'), (3139, 'magento'), (3140, 'variables'), (3141, 'templates'), (3142, 'dom'), (3143, 'table'), (3144, 'search'), (3145, 'cakephp'), (3146, 'pointers'), (3147, 'redirect'), (3148, 'powershell'), (3149, 'windows-phone-7'), (3150,'node.js'), (3151, 'tomcat'), (3152, 'web-applications'), (3153, 'optimization'), (3154, 'swing'), (3155, 'servlets'), (3156, 'qt'), (3157, 'authentication'), (3158, 'android-layout'), (3159, 'events'), (3160, 'jquery-mobile'), (3161, 'caching'), (3162, 'listview'), (3163, 'probability'), (3164, 'memory'), (3165, 'zend-framework'), (3166, 'java-ee'), (3167, 'css3'), (3168, 'inheritance'), (3169, 'gwt'), (3170, 'xslt'), (3171, 'math'), (3172, 'facebook-graph-api'), (3173, 'stored-procedures'), (3174, 'gui'), (3175, 'ms-access'), (3176, 'linq-to-sql'), (3177, 'iis7'), (3178, 'post'), (3179, 'reflection'), (3180, 'phonegap'), (3181, 'mobile'), (3182, 'grails'), (3183, 'activerecord'), (3184, 'file-upload'), (3185, 'razor'), (3186, 'browser'), (3187, 'gridview'), (3188, 'delphi'), (3189, 'google'), (3190, 'csv'), (3191, 'testing'), (3192, 'database-design'), (3193, 'memory-management'), (3194, 'vim'), (3195, 'select'), (3196, 'animation'), (3197, 'ssl'), (3198, 'ssh'), (3199, 'ios5'), (3200, 'cookies'), 
        (3201, 'scala'), (3202, 'iframe'), (3203, 'logging'), (3204, 'pdf'), (3205, 'blackberry'), (3206, 'curl'), (3207, 'mongodb'), (3208, 'layout'), (3209, 'asp.net-mvc-2'), (3210, 'file-io'), (3211, 'spring-mvc'), (3212, 'plugins'), (3213, 'excel-vba'), (3214, 'mvvm'), (3215, 'serialization'), (3216, 'drop-down-menu'), (3217, 'application'), (3218, 'windows-xp'), (3219, 'nhibernate'), (3220, 'core-data'), (3221, 'windows-server-2008'), (3222, 'jquery-plugins'), (3223, 'jsf-2'), (3224, 'asp-classic'), (3225, 'dynamic'), (3226, 'user-interface'), (3227, 'data-structures'), (3228, 'dns'), (3229, 'maven'), (3230, 'opencv'), (3231, 'netbeans'), (3232, 'scripting'), (3233, 'collections'), (3234, 'unicode'), (3235, 'script'), (3236, 'javascript-events'), (3237, 'encoding'), (3238, 'button'), (3239, 'printing'), (3240, 'version-control'), (3241, 'join'), (3242, 'xpath'), (3243, 'google-maps-api-3'), (3244, 'permissions'), (3245, 'abstract-algebra'), (3246, 'android-intent'), (3247, 'multidimensional-array'), (3248, 'haskell'), (3249, 'active-directory'), (3250,'nginx'), (3251, 'syntax'), (3252, 'datagridview'), (3253, 'div'), (3254, 'random'), (3255, 'web'), (3256, 'iphone-sdk-4.0'), (3257, 'opengl'), (3258, 'twitter-bootstrap'), (3259, 'canvas'), (3260, 'login'), (3261, 'jdbc'), (3262, 'image-processing'), (3263, 'jpa'), (3264, 'dictionary'), (3265, 'ant'), (3266, 'if-statement'), (3267, 'binding'), (3268, 'twitter'), (3269, 'backbone.js'), (3270, 'jqgrid'), (3271, 'architecture'), (3272, 'audio'), (3273, 'sequences-and-series'), (3274, 'complex-analysis'), (3275, 'geometry'), (3276, 'general-topology'), (3277, 'uitableviewcell'), (3278, 'jquery-selectors'), (3279, 'heroku'), (3280, 'ftp'), (3281, 'extjs'), (3282, 'time'), (3283, 'soap'), (3284, 'combinatorics'), (3285, 'asp.net-mvc-4'), (3286, 'exception-handling'), (3287, 'for-loop'), (3288, 'pdo'), (3289, 'dll'), (3290, 'statistics'), (3291, 'encryption'), (3292, 'sharepoint2010'), (3293, 'sqlite3'), (3294, 'drupal'), (3295, 'url-rewriting'), (3296, 'ado.net'), (3297, 'algebra-precalculus'), (3298, 'emacs'), (3299, 'google-chrome-extension'), (3300, 'group-theory'),
        (3301, 'deployment'), (3302, 'entity-framework-4'), (3303, 'uiwebview'), (3304, 'actionscript'), (3305, 'primefaces'), (3306, 'struts2'), (3307, 'character-encoding'), (3308, 'service'), (3309, 'vbscript'), (3310, 'checkbox'), (3311, 'knockout.js'), (3312, 'matrices'), (3313, 'autocomplete'), (3314, 'datagrid'), (3315, 'video'), (3316, 'graphics'), (3317, 'text'), (3318, 'utf-8'), (3319, 'amazon-ec2'), (3320, 'methods'), (3321, 'configuration'), (3322, 'types'), (3323, 'xhtml'), (3324, 'analysis'), (3325, 'recursion'), (3326, 'android-emulator'), (3327, 'language-agnostic'), (3328, 'macros'), (3329, 'https'), (3330, 'github'), (3331, 'usercontrols'), (3332, 'properties'), (3333, '.net-4.0'), (3334, 'php5'), (3335, 'batch'), (3336, 'upload'), (3337, 'batch-file'), (3338, 'stl'), (3339, 'error-handling'), (3340, 'input'), (3341, 'data'), (3342, 'groovy'), (3343, 'joomla'), (3344, 'xcode4'), (3345, 'foreach'), (3346, 'silverlight-4.0'), (3347, 'django-models'), (3348, 'arraylist'), (3349,'hash'), (3350, 'coding-style'), (3351, 'mfc'), (3352, 'interface'), (3353, 'vector'), (3354, 'opengl-es'), (3355, 'symfony2'), (3356, 'gcc'), (3357, 'boost'), (3358, 'asynchronous'), (3359, 'combobox'), (3360, 'triggers'), (3361, 'fonts'), (3362, 'casting'), (3363, 'routing'), (3364, 'frameworks'), (3365, 'orm'), (3366, 'localization'), (3367, 'coldfusion'), (3368, 'plsql'), (3369, 'website'), (3370, 'cron'), (3371, 'python-3.x'), (3372, 'limit'), (3373, 'python-2.7'), (3374, 'memory-leaks'), (3375, 'proxy'), (3376, 'uiview'), (3377, 'centos'), (3378, 'view'), (3379, 'tcp'), (3380, 'vb6'), (3381, 'sdk'), (3382, 'internet-explorer-8'), (3383, 'calendar'), (3384, 'azure'), (3385, 'windows-8'), (3386, 'terminal'), (3387, 'webview'), (3388, '.net-3.5'), (3389, 'insert'), (3390, 'graph'), (3391, 'activity'), (3392, 'map'), (3393, 'menu'), (3394, 'webserver'), (3395, 'reporting-services'), (3396, 'ruby-on-rails-3.1'), (3397, 'concurrency'), (3398, 'reference'), (3399, 'programming-languages'),(3400, 'sed'), 
        (3401, 'timer'), (3402, 'textbox'), (3403, 'installation'), (3404, 'parameters'), (3405, 'backup'), (3406, 'process'), (3407, 'compiler'), (3408, 'filesystems'), (3409, 'constructor'), (3410, 'model'), (3411, 'import'), (3412, 'air'), (3413, 'junit'), (3414, 'clojure'), (3415, 'io'), (3416, 'static'), (3417, 'internationalization'), (3418, 'ide'), (3419, 'tabs'), (3420, 'numpy'), (3421, 'windows-server-2003'), (3422, 'selenium'), (3423, 'safari'), (3424, 'amazon-web-services'), (3425, 'java-me'), (3426, 'uiviewcontroller'), (3427, 'mercurial'), (3428, 'visual-studio-2012'), (3429, 'matrix'), (3430, 'number-theory'), (3431, 'struct'), (3432, 'hyperlink'), (3433, 'uiscrollview'), (3434, 'svg'), (3435, 'debian'), (3436, 'resources'), (3437, 'attributes'), (3438, 'keyboard'), (3439, 'youtube'), (3440, 'delete'), (3441, 'dojo'), (3442, 'rss'), (3443, 'com'), (3444, 'formatting'), (3445, 'transactions'), (3446, 'eclipse-plugin'), (3447, 'jar'), (3448, 'download'), (3449,'oauth'), (3450, 'bluetooth'), (3451, 'f#'), (3452, 'amazon-s3'), (3453, 'tikz-pgf'), (3454, 'path'), (3455, 'ios6'), (3456, 'charts'), (3457, 'solr'), (3458, 'logic'), (3459, 'navigation'), (3460, 'rspec'), (3461, 'header'), (3462, 'functions'), (3463, 'filter'), (3464, 'c++11'), (3465, 'background'), (3466, 'maven-2'), (3467, 'mac'), (3468, 'colors'), (3469, 'smtp'), (3470, 'build'), (3471, 'tags'), (3472, 'microsoft-excel'), (3473, 'msbuild'), (3474, 'tfs'), (3475, 'windows-vista'), (3476, 'open-source'), (3477, '3d'), (3478, 'virtualbox'), (3479, 'functional-analysis'), (3480, 'module'), (3481, 'compilation'), (3482, 'crash'), (3483, 'automation'), (3484, 'jboss'), (3485, 'documentation'), (3486, 'wireless-networking'), (3487, 'assembly'), (3488, 'ip'), (3489, 'outlook'), (3490, 'usb'), (3491, 'vpn'), (3492, 'windows-server-2008-r2'), (3493, 'hard-drive'), (3494, 'hadoop'), (3495, 'dependency-injection'), (3496, '2010'), (3497, 'virtualization'), (3498, 'boot'), (3499, 'reference-request'),
        (3500, 'router'), (3501, 'misc')]

rendered_tags = []
search_string = ""
# Enter Server URL
server_url = "http://d0500832e17b.ngrok.io"

# This will work when debug is off!
# TO-DO Find good error pages
@app.errorhandler(500)
def internal_error(error):
    return "500 error"


@app.errorhandler(404)
def not_found(error):
    return "404 error", 404

@app.route("/register")
def register():
    ''' db = mysql.connector.connect(**conf)
    mycursor = db.cursor()

    sql = "INSERT INTO User (id, handle, email, password) VALUES (%s, %s, %s, %s)"
    val = ("1", "Cap", "shaileshborate@gmail.com", "12345678")
    mycursor.execute(sql, val)

    db.commit()

    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    db.close()
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
        cur.close()
        db.close()
        if account:
            session['id'] = account[0]
            session['username'] = account[1]
            session['email'] = account[2]
            msg = 'Logged in successfully!'
            flash(msg)
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
            flash(msg)
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('id', None)
    session.pop('username', None)
    session.pop('email', None)
    flash("Logged out successfully!")
    return redirect(url_for('home'))


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/askQuestion", methods=["GET", "POST"])
def askQuestion():
    if 'username' in session:
        if request.method == "POST":
            title = request.form.get("title")
            body = request.form.get("body")
            q = {"q": title}
            response = requests.post(server_url+"/tag", json=q).json()
            tags_list = response['tags']
            if not tags_list:
                tags_list.append("misc")
            query = ""
            for i in range(len(tags_list)-1):
                q = "SELECT Question.id, Question.title, Question.dop from Question,QuesTag,Tag WHERE Question.id=QuesTag.qid AND QuesTag.tid=Tag.id AND Tag.tag='{}'".format(tags_list[i])
                query = query+q+" UNION "
            q = "SELECT Question.id, Question.title, Question.dop from Question,QuesTag,Tag WHERE Question.id=QuesTag.qid AND QuesTag.tid=Tag.id AND Tag.tag='{}'".format(tags_list[-1])
            query = query+q

            db = mysql.connector.connect(**conf)

            cur = db.cursor()
            cur.execute(query)
            questions = cur.fetchall()

            duplicate_questions = []
            for question in questions:
                qs = {"q1": title, "q2": question[1]}
                response = requests.post(server_url+"/dup", json=qs).json()
                dup_score = response['prediction']
                print(dup_score)
                if dup_score >= 0.5:
                    duplicate_questions.append(question)
            if duplicate_questions:
                print(duplicate_questions)
                tags_list = []
                anscnt = []
                users = []
                for duplicate_question in duplicate_questions:
                    query = "select Tag.tag from Question,Tag,QuesTag where Question.id=QuesTag.qid and QuesTag.tid=Tag.id and Question.id={}".format(duplicate_question[0])
                    cur.execute(query)
                    tgs = cur.fetchall()
                    tags_list.append([t[0] for t in tgs])

                    query = "select count(*) from Question,QuesAns,Answer where Question.id=QuesAns.qid and QuesAns.aid=Answer.id and Question.id={}".format(duplicate_question[0])
                    cur.execute(query)
                    c = cur.fetchone()
                    anscnt.append(c[0])

                    query = "select User.id,User.handle from Question,User where Question.id={} and Question.uid=User.id".format(duplicate_question[0])
                    cur.execute(query)
                    u = cur.fetchall()
                    users.append(u[0])

                return render_template('ask.html',n=len(duplicate_questions), duplicate_questions=duplicate_questions, tags=tags_list, anscnt=anscnt, users=users)
            else:
                dop = datetime.now()
                cur.execute('INSERT INTO Question(uid,title,body,dop) values(%s,%s,%s,%s)',(session['id'], title, body, dop))
                qid = cur.lastrowid
                db.commit()

                tag_id = []
                for tag in tags_list:
                    for record in tags:
                        if tag == record[1]:
                            tag_id.append(record[0])
                            break
                for id in tag_id:
                    cur.execute('INSERT INTO QuesTag(qid,tid) values(%s,%s)', (qid, id))
                    db.commit()
                flash("Question posted successfully!")
                return redirect(url_for("quespage",id=qid))
            db.close()
            cur.close()
    else:
        return redirect(url_for('login'))
    return render_template('ask.html',n=0)


@app.route("/questions/<string:tag>", methods=["GET", "POST"])
def questions(tag):
    db = mysql.connector.connect(**conf)
    cur = db.cursor()
    if tag == "all":
        query = "select id,title,dop from Question"
    elif "_" in tag:
        tags_list=tag.split("_")
        tag=sub("_",", ",tag)
        query = ""
        q=" AND Question.id IN ("
        for i in range(len(tags_list)):
            query+="SELECT Question.id from Question,QuesTag,Tag WHERE Question.id=QuesTag.qid AND QuesTag.tid=Tag.id AND Tag.tag='{}'".format(tags_list[i])
            if i<len(tags_list)-1:
                query+=q
            else:
                query+=")"*(len(tags_list)-1)
        query="SELECT Question.id,Question.title,Question.dop from Question WHERE Question.id IN ("+query+")"
    else:
        for i,j in tags:
            if j==tag:
                tid=i
                break
        query = "select Question.id,Question.title,Question.dop from Question,QuesTag,Tag where Question.id=QuesTag.qid and QuesTag.tid=Tag.id and Tag.id={}".format(tid)
    cur.execute(query)
    ques = cur.fetchall()

    tags_list = []
    anscnt = []
    users = []
    for id, title, dop in ques:
        query = "select Tag.tag from Question,Tag,QuesTag where Question.id=QuesTag.qid and QuesTag.tid=Tag.id and Question.id={}".format(id)
        cur.execute(query)
        tgs = cur.fetchall()
        tags_list.append([t[0] for t in tgs])

        query = "select count(*) from Question,QuesAns,Answer where Question.id=QuesAns.qid and QuesAns.aid=Answer.id and Question.id={}".format(id)
        cur.execute(query)
        c = cur.fetchone()
        anscnt.append(c[0])

        query = "select User.id,User.handle from Question,User where Question.id={} and Question.uid=User.id".format(id)
        cur.execute(query)
        u = cur.fetchall()
        users.append(u[0])

    cur.close()
    db.close()
    return render_template("questions.html", ques=ques, n=len(ques), tags=tags_list, anscnt=anscnt, users=users, tag=tag)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if 'username' in session:
        db = mysql.connector.connect(**conf)
        cur = db.cursor()

        # Query for selecting questions posted by the user.
        query = "Select Question.id, Question.title, Question.dop from Question where Question.uid = {}".format(session['id'])
        cur.execute(query)
        ques = cur.fetchall()

        tags_list = []
        anscnt = []
        users = []
        for id, title, dop in ques:
            query = "select Tag.tag from Question,Tag,QuesTag where Question.id=QuesTag.qid and QuesTag.tid=Tag.id and Question.id={}".format(id)
            cur.execute(query)
            tgs = cur.fetchall()
            tags_list.append([t[0] for t in tgs])

            query = "select count(*) from Question,QuesAns,Answer where Question.id=QuesAns.qid and QuesAns.aid=Answer.id and Question.id={}".format(id)
            cur.execute(query)
            c = cur.fetchone()
            anscnt.append(c[0])

            query = "select User.id,User.handle from Question,User where Question.id={} and Question.uid=User.id".format(id)
            cur.execute(query)
            u = cur.fetchall()
            users.append(u[0])

        cur.close()
        db.close()
        return render_template('profile.html', ques=ques, n=len(ques), tags=tags_list, anscnt=anscnt, users=users)
    else:
        return redirect(url_for('login'))


@app.route("/tags/<int:page_no>/<flag>", methods=["GET", "POST"])
def tagpage(page_no, flag):
    global rendered_tags
    global search_string
    if request.method == "POST":
        search_string = request.form.get("tag")
        if search_string:
            search_string_lower = search_string.lower()
            rendered_tags = []
            for tag in tags:
                if tag[1].endswith(search_string_lower) or tag[1].startswith(search_string_lower):
                    rendered_tags.append(tag)
        else:
            rendered_tags = tags
    if flag == "True":
        rendered_tags = tags
        search_string = ""
    start = (page_no-1)*16
    end = min(len(rendered_tags), page_no*16)
    end_page = math.ceil(len(rendered_tags)/16)
    return render_template("tags.html", tags=rendered_tags, start=start, end=end, page_no=page_no, end_page=end_page, search_string=search_string, n=len(rendered_tags))

@app.route("/ques/<int:id>")
def quespage(id):
    db = mysql.connector.connect(**conf)
    cur = db.cursor()
    query = "select id,title,body,dop from Question where id={}".format(id)
    cur.execute(query)
    ques = cur.fetchone()
    id,title,body,dop=ques[0],ques[1],ques[2],ques[3].strftime("%d-%b-%Y %H:%M")

    query = "select Tag.tag from Question,Tag,QuesTag where Question.id=QuesTag.qid and QuesTag.tid=Tag.id and Question.id={}".format(id)
    cur.execute(query)
    tgs = cur.fetchall()
    tgs=[t[0] for t in tgs]

    query = "select count(*) from Question,QuesAns,Answer where Question.id=QuesAns.qid and QuesAns.aid=Answer.id and Question.id={}".format(id)
    cur.execute(query)
    c = cur.fetchone()[0]

    query = "select User.id,User.handle from Question,User where Question.id={} and Question.uid=User.id".format(id)
    cur.execute(query)
    uq = cur.fetchone()

    query = "select Answer.*,User.handle from Answer,QuesAns,User where QuesAns.qid={} and Answer.uid=User.id".format(id)
    cur.execute(query)
    ans = cur.fetchall()

    cur.close()
    db.close()
    return render_template("quespage.html",tgs=tgs,c=c,uq=uq,ques=[id,title,body,dop],ans=ans,n=len(ans))

@app.route("/searchQuestion", methods=["GET", "POST"])
def searchQuestion():
    if request.method == "POST":
        question_query = request.form.get("question")
        q = {"q": question_query}
        response = requests.post(server_url+"/tag", json=q).json()
        tags_list = response['tags']
        if not tags_list:
            tags_list.append("misc")
        query = ""
        for i in range(len(tags_list)-1):
            q = "SELECT Question.id, Question.title, Question.dop from Question,QuesTag,Tag WHERE Question.id=QuesTag.qid AND QuesTag.tid=Tag.id AND Tag.tag='{}'".format(tags_list[i])
            query = query+q+" UNION "
        q = "SELECT Question.id, Question.title, Question.dop from Question,QuesTag,Tag WHERE Question.id=QuesTag.qid AND QuesTag.tid=Tag.id AND Tag.tag='{}'".format(tags_list[-1])
        query = query+q

        db = mysql.connector.connect(**conf)

        cur = db.cursor()
        cur.execute(query)
        questions = cur.fetchall()

        duplicate_questions = []
        for question in questions:
            qs = {"q1": question_query, "q2": question[1]}
            response = requests.post(server_url+"/dup", json=qs).json()
            dup_score = response['prediction']
            print(dup_score)
            if dup_score >= 0.5:
                duplicate_questions.append(question)
        if duplicate_questions:
            print(duplicate_questions)
            tags_list = []
            anscnt = []
            users = []
            for duplicate_question in duplicate_questions:
                query = "select Tag.tag from Question,Tag,QuesTag where Question.id=QuesTag.qid and QuesTag.tid=Tag.id and Question.id={}".format(duplicate_question[0])
                cur.execute(query)
                tgs = cur.fetchall()
                tags_list.append([t[0] for t in tgs])

                query = "select count(*) from Question,QuesAns,Answer where Question.id=QuesAns.qid and QuesAns.aid=Answer.id and Question.id={}".format(duplicate_question[0])
                cur.execute(query)
                c = cur.fetchone()
                anscnt.append(c[0])

                query = "select User.id,User.handle from Question,User where Question.id={} and Question.uid=User.id".format(duplicate_question[0])
                cur.execute(query)
                u = cur.fetchall()
                users.append(u[0])

            return render_template('searchQuestion.html',n=len(duplicate_questions), duplicate_questions=duplicate_questions, tags=tags_list, anscnt=anscnt, users=users,type_of_request="POST",search_question=question_query)
        else:
            return render_template('searchQuestion.html',n=0,type_of_request="POST",search_question=question_query)
    else:
        return render_template('searchQuestion.html',n=0,type_of_request="GET",search_question="")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
