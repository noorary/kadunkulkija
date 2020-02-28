from application import app, db
from flask import redirect, render_template, request, url_for, Flask
from flask_paginate import Pagination, get_page_args
from application.streets.models import Street
from application.auth.models import User

@app.route("/stats", methods=["GET"])
def stats_index():


    return render_template("/stats/stats.html", has_visited=User.find_users_with_fiveormore_completed(), many_plans=Street.find_streets_in_many_plans())