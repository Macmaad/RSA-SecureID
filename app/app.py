import os 
import json 
from functools import wraps

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_cors import CORS

from final_rsa import rsa_generator, fast_exp_handler


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
CORS(app)
PIN = 4567


def is_logged_in(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return function(*args, **kwargs)
        else:
            flash("Unauthorized, please login", "danger")
            return redirect(url_for("login"))

    return wrap


@app.route("/token", methods=["GET", "POST"])
def generate_token(): 
    if request.method == "POST": 
        users_input = int(request.form["val"]) if request.form["val"] else 0
        if users_input and fast_exp_handler(users_input, int(os.environ["private_key"]), int(os.environ["module_n"])) == PIN: 
            session["logged_in"] = True
            flash("You are now logged in", "success")
        else: 
            flash("Error in the pin", "danger")
        return render_template("index.html")
    elif request.method == "GET": 
        module_n, public_key, private_key = rsa_generator() 
        os.environ["module_n"] = str(module_n)
        os.environ["private_key"] = str(private_key)
        os.environ["public_key"] = str(public_key)
        encrypted_pin = fast_exp_handler(PIN, public_key, module_n)
        response = {"status_code": 200, "body": {"pin": str(encrypted_pin), "message": "OK"}}
    else: 
        response = {"status_code": 400, "body": {"message": "BAD REQUEST"}}
    return response 


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    flash("You are now logged out.", "danger")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.secret_key = "ultra_secret_123"
    app.run(debug=True)