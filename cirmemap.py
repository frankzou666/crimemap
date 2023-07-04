from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

APP_PORT= 5001
DB_NAME= "crime"
DB_HOST='127.0.0.1'
DB_PORT=27001
DB_USER='app'
DB_PWD='app123456'


app = Flask(__name__)

DB = DBHelper(db_host=DB_HOST,db_port=DB_PORT,db_user=DB_USER,db_password=DB_PWD,db_name=DB_NAME)

@app.route("/")
def home():
    try:
           data = DB.get_all_inputs()
    except Exception as e:
           print(e)
           data = None
    return render_template("home.html", data=data)

@app.route("/add", methods=["POST"])
def add():
     try:
       data = request.form.get("userinput")
       DB.add_input(data)
     except Exception as e:
       print(e)
     return home()

@app.route("/clear")
def clear():
    try:
       DB.clear_all()
    except Exception as e:
       print(e)

    return home()

if __name__ == '__main__':
     app.run(port=APP_PORT, debug=True)
