#from dbm import _Database
from flask import Flask, render_template
from flask import render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

cursor = mysql.connection.cursor()
print(cursor)
#Executing SQL Statements
cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()
 
#Closing the curso
cursor.close()

@app.route('/')
def home():
    return render_template("dashtemp.html")

#connection to database
@app.route('/login')
def form():
    return render_template('summary.html')





@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 

    
@app.route('/buyticket')
def tciket():
    return render_template("slot.html")

    
    return render_template('slot.html')

if __name__=='__main__':
    app.run(debug=True)