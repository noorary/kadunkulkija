from application import app, db
from flask import redirect, render_template, request, url_for
from application.streets.models import Street

@app.route("/streets", methods=["GET"])
def streets_index():
	return render_template("/streets/list.html", streets = Street.query.all())

@app.route("/streets/newstreet/")
def street_form():
    return render_template("streets/newstreet.html")

@app.route("/streets/", methods=["POST"])
def street_add():
    s = Street(request.form.get("name"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("streets_index"))
