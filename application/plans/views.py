from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.plans.models import Plan
from application.plans.forms import PlanForm

@app.route("/myplans", methods=["GET"])
@login_required
def myplan_index():
    return render_template("/plans/plans.html")

@app.route("/myplans/", methods=["POST", "GET"])
# @login_required
def plan_add():

    if request.method == 'GET':
        return render_template("/plans/newplan.html", form = PlanForm())

    else:

        form = PlanForm(request.form)

        p = Plan(form.date.data)
        p.account_id = current_user.id 
        # p.street_id = form.street.data
        p.completed = false

        db.session.add(p)
        db.session.commit()

        return redirect(url_for("myplan_index"))

        


    
