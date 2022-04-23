from flask import Flask, render_template
from flask import render_template,request,redirect, url_for




app = Flask(__name__)


@app.route('/')
def home():
    return render_template("dashtemp.html")

    
@app.route('/ticket')
def tciket():
    return render_template('slot.html')

if __name__=='__main__':
    app.run(debug=True)