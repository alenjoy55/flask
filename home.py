from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

@app.route('/')
def fun1():
    return "helloflask"

@app.route('/fun2',methods=['POST','GET'])
def fun2():
    if request.method=='POST':
        name=request.form['name']
        place=request.form['place']
        print(name,place)
        con=sqlite3.connect("user.db")
        # con.execute("create table user(name text,place text)")
        con.execute("insert into user(name,place)values(?,?)",(name,place))
        con.commit()


    a=20
    return render_template('index.html',data=a)

app.run()