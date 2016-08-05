# -*- coding: utf-8 -*-
from flask import render_template, Blueprint, flash, request, redirect,Flask
from flask_wtf import Form
from wtforms import (StringField, BooleanField, TextAreaField, SubmitField,
                     validators, ValidationError)
from flask_mail import Mail, Message
from contact import contact_form

from passwords import *

mail = Mail()

app = Flask(__name__)

# initialise config file
app.config.from_object('config')

mail.init_app(app)

@app.route("/")
def index():
    title = "Welcome"

    return render_template('index.html', title = title)

@app.route("/feed/")
def feed():
    title = 'Feed'

    return render_template('feed.html', title = title)

@app.route('/personal/')
def personal():
    title = 'Personal'

    return render_template('personal/personal.html', title = title)

@app.route('/personal/elisabeth_gr/')
def elisabeth_gr():
    title = "Elisabeth"

    return render_template('personal/elisabeth_gr.html', title = title)


@app.route('/personal/elisabeth_rus/')
def elisabeth_rus():
    title = "Elisabeth"

    return render_template('personal/elisabeth_rus.html', title = title)


@app.route('/personal/poem_rus/')
def poem_rus():
    title = 'Kelesidis D.'

    return render_template('personal/poem_rus.html', title = title)

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    title = "Contact"
    form = contact_form()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("contact.html",form=form)

        else:
            msg = Message(form.name.data, sender = 'levan@kelesidis.de', recipients = ['levan@kelesidis.de'] )
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact_success.html')
    elif request.method == "GET":
        return render_template("contact.html", form=form)


@app.route("/contact_success/")
def contact_success():
    title = "Message sent"

    return render_template("contact_success.html", title=title)


if __name__ == "__main__":
    app.run( debug = True)