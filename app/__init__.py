# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run( debug = True)