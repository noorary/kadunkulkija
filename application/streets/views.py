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

@app.route("/streets/newstreet/")
@login_required
def street_form():
    #Kokeilu
    #districts_database = District.query.with_entities(District.id, District.name)
    #districts_field = [(x.id, x.name) for x in districts_database]
    return render_template("streets/newstreet.html", form = StreetForm())

@app.route("/streets/", methods=["POST"])
def street_add():
    form  = StreetForm(request.form)

    if not form.validate():
        return render_template("streets/newstreet.html", form = form)

    
    

    new_street = Street(form.name.data)
    new_street.district_id = form.district.data

    db.session().add(new_street)
    db.session().commit()

    return redirect(url_for("streets_index"))

@app.route("/streets/edit/<street_id>", methods=["GET"])
# @login_required
def edit_street_name(street_id):

    form = EditStreetForm(request.form)

    return render_template("streets/editname.html", street = Street.query.get(street_id), form=form)


@app.route("/streets/edit/", methods=["GET"])
# @login_required
def street_edit():



    return render_template("streets/editlist.html/", streets = Street.query.all() )

@app.route("/streets/edit/ready/<street_id>", methods=["POST"])
def set_new_name(street_id):

    form = EditStreetForm(request.form)

    s = Street.query.get(street_id)
    new = form.newname.data

    s.name = new
    db.session().commit()

    return redirect(url_for("streets_index"))
