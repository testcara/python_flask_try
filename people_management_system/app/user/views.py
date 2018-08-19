from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from . import user
from forms import UserForm, FindUserForm
from app import db
from app import User
 


@user.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
 
    print form.errors
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Created Successfully!')
        return render_template('user/show_user.html', user = user, title='show_user')

    return render_template('user/create_user.html', form=form)

@user.route('/find_user', methods=['GET', 'POST'])
def find_user():
    form = FindUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
                user = User.query.filter_by(email=form.email.data).first()
                if user != None:
                    flash('Find the user!')
                    return render_template('user/show_user.html', user=user)
                else:
                    flash("No such user in the database!")
           
    return render_template("user/find_user.html", form=form)

@user.route('/show_users')
def show_users():
    users = User.query.order_by(User.username).all()
    return render_template('user/show_users.html', users = users)
