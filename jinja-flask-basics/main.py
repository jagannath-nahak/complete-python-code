from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    marks={
        "Abhas":29,
        "sohan":40,
        "alok":80,
        "guru":59,
        "ranjan":80,
        "Biswa":100,
        "sitaram":95,
        "sweta":84
    }  
    return render_template("index.html",marks=marks)

app.run(debug=True)