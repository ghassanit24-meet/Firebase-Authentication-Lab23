from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyBeqzh98gRmsc_q2CbDhBMu8jPzMhLR_Cw",
  "authDomain": "ghassan-300a1.firebaseapp.com",
  "projectId": "ghassan-300a1",
  "storageBucket": "ghassan-300a1.appspot.com",
  "messagingSenderId": "121007362148",
  "appId": "1:121007362148:web:dd47ba78de35d8843d8f71",
  "measurementId": "G-4HYWBJN6RZ"
  "databaseURL": ""
}

@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = "Oops, we seemed to have run into a problem"
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = 
                auth.create_user_with_email_and_password(email, password)
            return redirect(url_for("add_tweet"))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    error = "Oh no! It seems like we can't sign in"
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']=
                auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for("add_tweet"))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)