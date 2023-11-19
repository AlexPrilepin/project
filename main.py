from flask import Flask, render_template, url_for, jsonify, request, redirect, session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(248)
a = {"root": "pass"}




#@login_required
@app.route('/<username>')
def main(username):
    global a
    print(username)
    if username not in a.keys():
        return redirect("http://localhost:5000/login/", code=302)
    return render_template("ez.html")



@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
            return redirect(f"http://localhost:5000/{username}", code=302)
        else:
            message = "Wrong username or password"

    return render_template("login.html", message=message)





@app.route('/')
def hi():
    return redirect("http://localhost:5000/login/", code=302)


app.run(debug=True)





app.run(debug=True)
