from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, current_app
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.Models.association_table import User
from app import db, admin_permission
from flask_principal import Identity, identity_changed

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/signup', methods=['POST',"GET", "POST"])
@admin_permission.require()
def signup_post():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address signed up.')
            return redirect(url_for('login.signup_post'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, password=generate_password_hash(password, method='sha256'), role=role)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login.log_in'))
    return render_template('signup.html')

@login.route('/login', methods=["GET", "POST"])
def log_in():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login.log_in')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.role))
        return redirect(url_for('customer_quote.view_quotations'))

    return render_template('login.html')