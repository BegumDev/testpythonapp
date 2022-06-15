from flask import render_template, request, redirect, url_for
from financetracker import app, db
from financetracker.models import Customer


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/myaccount")
def myaccount():
    info = list(Customer.query.all())
    return render_template("myaccount.html", info=info)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        details = Customer(
            full_name=request.form.get("full_name"),
            age=request.form.get("age")
        )
        db.session.add(details)
        db.session.commit()
        return redirect(url_for("myaccount"))
    return render_template("register.html")