from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db #, login_required
from application.districts.models import District
from application.districts.forms import DistrictForm

@app.route("/districts", methods=["GET"])
def districts_index():
    return render_template("/districts/list.html", districts = District.query.all())

@app.route("/districts/newdistrict/")
@login_required
def district_form():
    return render_template("districts/newdistrict.html", form = DistrictForm())

@app.route("/districts/", methods=["POST"])
def district_add():
    form = DistrictForm(request.form)

    if not form.validate():
        return render_template("districts/newdistrict.html", form = form)

    d = District(form.name.data)

    db.session().add(d)
    db.session().commit()

    return redirect(url_for("districts_index"))
