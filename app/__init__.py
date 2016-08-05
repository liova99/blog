# -*- coding: utf-8 -*-
from flask import render_template, Blueprint, flash, request, redirect,Flask
from flask_wtf import Form
from wtforms import (StringField, BooleanField, TextAreaField, SubmitField,
                     validators, ValidationError)
from flask_mail import Mail, Message
from contact import contact_form

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'levan.list@gmail.com'
app.config["MAIL_PASSWORD"] = ''

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
            msg = Message(form.name.data, sender = 'levan.list@gmail.com', recipients = ['levan.kelesidis@gmail.com'] )
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return "Message was successfully sent"#, sleep(3), redirect('http://kelesidis.de/')
    elif request.method == "GET":
        return render_template("contact.html", form=form)



if __name__ == "__main__":
    app.run( debug = True)