from application import app, db
from flask import redirect, render_template, request, url_for, Flask
from flask_login import login_required
from application.streets.models import Street
from application.streets.forms import StreetForm
from application.streets.forms import EditStreetForm
from flask_paginate import Pagination, get_page_args
from application.districts.models import District


@app.route("/streets", methods=["GET"])
def streets_index():

    streets = Street.query.order_by(Street.name).all()

    def get_streets(offset=0, per_page=10):
        return streets[offset: offset + per_page]

    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")

    total = len(streets)

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework="bootstrap4", record_name="streets")


    paginated_streets = get_streets(offset=offset, per_page=per_page)

    return render_template("/streets/list.html", streets = paginated_streets, page=page, per_page=per_page, pagination=pagination)

    

@app.route("/streets/newstreet/", methods=["GET", "POST"])
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

    name = Street.query.filter_by(id = street_id)
    form = EditStreetForm(request.form)

    

    return render_template("streets/editname.html", street = Street.query.get(street_id), form=form, name = name)


@app.route("/streets/edit/", methods=["GET"])
@login_required
def street_edit():

    streets = Street.query.all()

    def get_streets(offset=0, per_page=10):
        return streets[offset: offset + per_page]

    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")

    total = len(streets)

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework="bootstrap4", record_name="streets")


    paginated_streets = get_streets(offset=offset, per_page=per_page)
    
    return render_template("streets/editlist.html/", streets = paginated_streets, page=page, per_page=per_page, pagination=pagination)

@app.route("/streets/edit/ready/<street_id>", methods=["POST"])
@login_required
def set_new_name(street_id):

    form = EditStreetForm(request.form)

    s = Street.query.get(street_id)
    new = form.newname.data

    s.name = new
    db.session().commit()

    return redirect(url_for("streets_index"))

@app.route("/streets/delete/<street_id>", methods=["POST"])
@login_required
def delete_street(street_id):

    id = street_id
    stmnt = 'DELETE FROM street WHERE street.id = ' + id
    stmnt2 = 'DELETE FROM street_plan WHERE street_id = ' + id
    db.engine.execute(stmnt)
    db.engine.execute(stmnt2)
    db.session.commit()

    return redirect(url_for('streets_index'))
