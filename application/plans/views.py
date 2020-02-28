from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.plans.models import Plan, street_plan
from application.plans.forms import PlanForm, MoreStreets
from application.streets.models import Street
from sqlalchemy.sql import text
from flask_paginate import Pagination, get_page_args
from application.plans.models import streets_in_plan

@app.route("/myplans", methods=["GET"])
@login_required
def myplan_index():

    return render_template("/plans/plans.html", plans = Plan.query.order_by(Plan.plandate).all())
    

@app.route("/myplans/newplan", methods=["POST", "GET"])
@login_required
def plan_add():

    streets = Street.query.all()
    street_list = [(s.id, s.name) for s in streets]

    form = PlanForm(request.form)
    form.street.choices = street_list

    if request.method == "GET":
        return render_template("plans/newplan.html", form = form)

    if request.method == "POST":


        new_plan = Plan() 

        new_plan.completed = False
        new_plan.plandate = form.plandate.data
        new_plan.account_id = current_user.id

        db.session().add(new_plan)
        db.session().commit()

        streets_in_plan = [form.street.data]

        for i in streets_in_plan:
            statement = street_plan.insert().values(street_id=i, plan_id=new_plan.id)
            db.session.execute(statement)
        db.session.commit()
        return redirect(url_for("myplan_index"))

@app.route("/myplans/<plan_id>/", methods=["POST"])
def plan_set_completed(plan_id):

    p = Plan.query.get(plan_id)
    p.completed = True
    db.session().commit()

    return redirect(url_for("myplan_index"))

@app.route("/myplans/delete/<plan_id>", methods=["POST"])
def delete_plan(plan_id):
    id = plan_id
    stmnt = 'DELETE FROM plan WHERE plan.id = ' + id 
    stmnt2 = 'DELETE FROM street_plan WHERE street_plan.plan_id = ' + id
    db.engine.execute(stmnt2)
    db.engine.execute(stmnt)
    db.session.commit()

    return redirect(url_for("myplan_index"))

@app.route("/myplans/addmore/<plan_id>", methods=["GET", "POST"])
@login_required
def add_many_streets(plan_id):

    plan = Plan.query.get(plan_id)

    form = MoreStreets(request.form)

    streets = Street.query.all()
    street_list = [(s.id, s.name) for s in streets]

    form.street.choices = street_list

    if request.method == "GET":

        return render_template("/plans/morestreets.html", form = form, plan = plan)

    if request.method == "POST":

        street_to_add = [form.street.data]

        for i in street_to_add:
            statement = street_plan.insert().values(street_id=i, plan_id=plan_id)
            db.session.execute(statement)
        db.session.commit()

        return redirect(url_for("myplan_index"))

@app.route("/myplans/show/<plan_id>", methods=["GET"])
def plan_show_streets(plan_id):

    plan_to_show_id = Plan.query.get(plan_id).id
    streets_to_show = streets_in_plan(plan_id)

    return render_template("plans/plans.html",
                            plans=Plan.query.all(),
                            selected_plan_id=plan_to_show_id,
                            selected_plan_streets = streets_to_show)

    

    
    
