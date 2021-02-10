from flask import render_template, redirect, url_for, request
from bs4 import BeautifulSoup
from app.room import create_random_room, get_room, activate_room
from app import app

import logging

log = logging.getLogger(__name__)


def prettify(html):
    return BeautifulSoup(html, "html.parser").prettify()


@app.route("/")
@app.route("/index")
def index():
    return prettify(render_template("index.html"))


@app.route("/room/new")
def new_room():
    code = create_random_room()
    if code:
        return redirect(url_for("room", room_code=code))
    return redirect(url_for("index"))


@app.route("/room/button")
def button_down():
    code = request.args.get("room_code", None)
    return activate_room(code)


@app.route("/room")
def room():
    code = request.args.get("room_code", None)
    room = get_room(code)
    if room:
        code = code.upper()
        return prettify(
            render_template(
                "room.html",
                room_code=code,
                activation_reset=app.config["ACTIVATION_RESET_MS"],
            )
        )
    return redirect(url_for("index"))
