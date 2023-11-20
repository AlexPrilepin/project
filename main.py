from flask import Flask, render_template, url_for, jsonify, request, redirect, session
from output_chaser import tests_operator
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(248)
a = {"root": "pass"}
b = {"root" : {1: -1}}

@app.route('/')
def hi():
    return redirect("http://localhost:5000/login/", code=302)






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


@app.route('/<username>', methods=['post', 'get'])
def main(username):
    global a
    results = b[username]
    if username not in a.keys():
        return redirect("http://localhost:5000/login/", code=302)
    if request.method == "POST":
        code = request.form.get('useless_text')
        result = tests_operator(code, "good_test.py", "tests_1.txt")
        b[username][1] = max(result, b[username][1])
        print(b[username])
    return render_template("ez.html", results=results)



app.run(debug=True)





