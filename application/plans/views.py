from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.plans.models import Plan
from application.plans.forms import PlanForm
from application.streets.models import Street

@app.route("/myplans", methods=["GET", "POST"])
 #@login_required
def myplan_index():
    return render_template("/plans/plans.html")

@app.route("/myplans/newplan", methods=["POST", "GET"])
# @login_required
def plan_add():


    streets = Street.query.all()
    street_list = [(s.id, s.name) for s in streets]

    form = PlanForm(request.form)
    form.street.choices = street_list

    if form.validate_on_submit():
        new_plan = Plan(form.plandate.data, form.street.data)
        new_plan.account_id = current_user.id 


        db.session().add(new_plan)
        db.session().commit()

        return redirect(url_for("myplan_index"))


    return render_template("plans/newplan.html", form = form)



    
