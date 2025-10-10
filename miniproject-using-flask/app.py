from flask import Flask,request,render_template,redirect

app=Flask(__name__)
items=[]
@app.route("/")
def home():
    return render_template("index.html",items=items)

@app.route("/add",methods=["post"])
def add_item():
    item=request.form.get("item")
    if item:
        items.append(item)
    return redirect("/")
@app.route("/delete/<int:index>")
def delete_item(index):
    if 0<= index <len(items):
        items.pop(index)
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)