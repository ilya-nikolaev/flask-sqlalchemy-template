from flask import Flask
from flask import request, session, g
from flask import render_template, flash, redirect

from db.funcs.auth import check_user


def sign_in_view():
    if request.method == "GET":
        return render_template("sign_in.html")

    username = request.form.get("username").strip()
    password = request.form.get("password").strip()

    user_id = check_user(g.db, username, password)
    if user_id is None:
        print("...")
        flash("Wrong username or password")
        return render_template("sign_in.html")

    session.update({"user_id": user_id})
    return redirect("/")


def register_auth_views(app: Flask):
    app.add_url_rule("/sign_in", "sign_in", sign_in_view, methods=["GET", "POST"])
