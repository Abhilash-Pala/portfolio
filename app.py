from flask import Flask, request, render_template, redirect, url_for, session, flash, send_file
from flask_session import Session
from itsdangerous import URLSafeTimedSerializer
import mysql.connector

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
mydb = mysql.connector.connect(host="localhost", user="root", password="Admin", database="portfolio")

@app.route("/",methods=["GET","POST"])
def home():
    
        return render_template('home.html')
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        Comment = request.form['Comment']
        cursor = mydb.cursor(buffered=True)
        cursor.execute('INSERT INTO c_form (name, email, Comment) VALUES (%s, %s, %s)', (name, email, Comment))
        mydb.commit()
        cursor.close()
        return redirect(url_for('contact'))
    return render_template('home.html')


@app.route('/download_resume')
def download_resume():
    #  return 'hi'
    path = "templates/Abhilash-Resume.pdf"  # Path to your resume file
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
