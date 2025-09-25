from flask import Flask,flash,render_template

app=Flask(__name__)

app.secret_key="1nq298defbiujbi98froihfhuf"

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!","success")
    return render_template("logout.html")

app.run(debug=True)