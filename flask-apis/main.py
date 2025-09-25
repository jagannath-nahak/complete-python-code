from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/")
def json():
    marks={
        "name":"jaga",
        "age":20,
        "section":"20A",
    }
    values=[1,marks,24]
    return jsonify(values)

app.run(debug=True)