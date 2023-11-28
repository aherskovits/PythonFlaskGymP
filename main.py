
from flask import Flask, request, render_template, redirect,url_for
import sqlite3

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template("index.html")

def insert():
    print("insert activity time age and director")
    iactivity = input('activity')
    itime = input('time')
    iage = input('age')
    idirector = input('director')
    conn = sqlite3.connect('GYMDB.db')
    c = conn.cursor()
    c.execute("create table if not exists pinformation(activity text,time text,age text,director text,participents text)")
    try:
        c.execute('INSERT INTO pinformation (activity, time, age, director) VALUES (?, ?, ?, ?)', (iactivity, itime, iage, idirector))
        conn.commit()
        conn.close()
        print("added to db")
    except:
        print("faild, try again")


# insert()


@app.route("/register", methods=['GET', 'POST'])
def goto():
    return render_template('register.html')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        factivity = request.form['activity']
        fage = request.form['age']
        ftime = request.form['time']
        fdirector = request.form['director']
        conn = sqlite3.connect('GYMDB.db')
        c = conn.cursor()
        c.execute("SELECT * FROM pinformation WHERE activity=? OR time=? OR age=? OR director=?", (factivity, ftime, fage, fdirector))
        data = c.fetchall()
        conn.close()
        return render_template("aPage.html", rows=data)
    else:
        print('not allowed')


@app.route('/register', methods=['GET', 'POST'])
def regis():
    # if request.method == 'GET':
    if request.method == 'POST':
        firstname = request.form['firstname', False]
        lastname = request.form['lastname']
        age = request.form['age']
        email = request.form['email']
        phone = request.form['phone']
        ptime = request.form['time']
        pactivity = request.form['activity']

        conn = sqlite3.connect('GYMDB.db')
        c = conn.cursor()
        c.execute("create table if not exists adetails(firstname text,lastname text,email text,phone text,age text,time text, activity text)")
        c.execute('INSERT INTO adetails (firstname, lastname, email, phone, age, time, activity) VALUES (?, ?, ?, ?, ?, ?, ?)', (firstname, lastname, email, phone, age, ptime, pactivity))
        conn.commit()
        c.execute("SELECT activity,time FROM pinformation WHERE activity=? AND time=?",(pactivity,ptime))
        rows = c.fetchall()
        mmessage = 'successfully registered'
        if len(rows) == 0:
            mmessage = 'no activity error'
        conn.close()
        return render_template('register.html', message=mmessage, rows=rows)

    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
 