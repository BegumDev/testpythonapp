from flask import render_template, request, redirect, url_for
from financetracker import app, db
from financetracker.models import Customer


# Display the homepage
@app.route("/")
def home():
    return render_template("base.html")

# 1. View all users
@app.route("/view_users")
def view_users():
    info = Customer.query.all()
    return render_template("view_users.html", info=info)


# 2. Create a user to the database
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        details = Customer(
            full_name=request.form.get("full_name"),
            age=request.form.get("age")
        )
        db.session.add(details)
        db.session.commit()
        return redirect(url_for("view_users"))
    return render_template("add_user.html")


#3. Edit a user
@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = Customer.query.get_or_404(user_id)
    if request.method == "POST":
        user.full_name = request.form.get("full_name")
        user.age = request.form.get("age")
        db.session.commit()
        return redirect(url_for("view_users"))
    return render_template('edit_user.html', user=user)


#4. Delete a user
@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = Customer.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return render_template('view_users.html')
