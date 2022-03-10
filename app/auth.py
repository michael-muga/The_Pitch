from . import auth
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Pitch, Comment
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user

from flask_wtf import FlaskForm
from .main.forms import LoginForm, RegisterForm, PitchForm, CommentForm


from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    # getting info from form
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:

            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.dashboard'))

    return render_template("signup.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    pitch = Pitch.query.all()

    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(owner_id=current_user.id, content=form.content.data)
        form.content.data = ''

        db.session.add(comment)
        db.session.commit()
    return render_template('dashboard.html', name=current_user.username, pitch=pitch, form=form, content=form.content.data)