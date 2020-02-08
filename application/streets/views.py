from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.streets.models import Street
from application.streets.forms import StreetForm
from application.streets.forms import EditStreetForm

from application.districts.models import District

@app.route("/streets", methods=["GET"])
def streets_index():
	return render_template("/streets/list.html", streets = Street.query.all())

@app.route("/streets/newstreet/", methods=("GET", "POST"))
@login_required
def street_form():

    districts = District.query.all()
    district_list = [(d.id, d.name) for d in districts]

    form = StreetForm(request.form)
    form.district.choices = district_list

    if form.validate_on_submit():

        new_street = Street(form.name.data)
        new_street.district_id = form.district.data

        db.session().add(new_street)
        db.session().commit()

        return redirect(url_for("streets_index"))
    
    return render_template("streets/newstreet.html", form = form)

    

@app.route("/streets/edit/<street_id>", methods=["GET"])
@login_required
def edit_street_name(street_id):

    form = EditStreetForm(request.form)

    return render_template("streets/editname.html", street = Street.query.get(street_id), form=form)


@app.route("/streets/edit/", methods=["GET"])
@login_required
def street_edit():



    return render_template("streets/editlist.html/", streets = Street.query.all() )

@app.route("/streets/edit/ready/<street_id>", methods=["POST"])
@login_required
def set_new_name(street_id):

    form = EditStreetForm(request.form)

    s = Street.query.get(street_id)
    new = form.newname.data

    s.name = new
    db.session().commit()

    return redirect(url_for("streets_index"))
