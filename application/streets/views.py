from application import app
from flask import render_template, request

@app.route("/streets/newstreet/")
def street_form():
    return render_template("streets/newstreet.html")

@app.route("/streets/", methods=["POST"])
def street_add():
    print(request.form.get("name"))
  
    return "hello world!"
