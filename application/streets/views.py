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

@app.route("/streets/edit/<street_id>", methods=["GET"])
def edit_street_name(street_id):

    return render_template("streets/editname.html", street = Street.query.get(street_id))


@app.route("/streets/edit/", methods=["GET"])
def street_edit():

    return render_template("streets/editlist.html/", streets = Street.query.all() )

@app.route("/streets/edit/ready/<street_id>", methods=["POST"])
def set_new_name(street_id):

    s = Street.query.get(street_id)
    new = request.form.get("newname")

    s.name = new
    db.session().commit()

    return redirect(url_for("streets_index"))
