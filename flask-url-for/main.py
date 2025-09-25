from flask import Flask,render_template

# app=Flask(__name__,static_url_path="/public") this is how changing static url path
app=Flask(__name__,static_folder="assets",static_url_path="/static")

@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(debug=True)