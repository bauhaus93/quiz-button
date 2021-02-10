import random
import string
import time
import logging

from app import app, db
from app.models import Room

log = logging.getLogger(__name__)


def clear_rooms(threshold):
    log.info(f"Removing inactive rooms, threshold {threshold}s")
    min_time = int(time.time()) - threshold
    inactive_rooms = Room.query.filter(Room.last_activation < min_time).all()
    for r in inactive_rooms:
        db.session.delete(r)
    db.session.commit()
    log.info(f"Removed {len(inactive_rooms)} inactive rooms")


def get_room(code):
    if code:
        return Room.query.filter_by(id=code.upper()).first()
    return None


def activate_room(code):
    room = get_room(code)
    if room:
        if int(time.time()) - room.last_activation >= 3:
            room.last_activation = int(time.time())
            room.placement = 0
        room.placement += 1
        db.session.commit()
        return str(room.placement)
    return "0"


def create_random_room():
    for i in range(3):
        try:
            code = "".join(random.sample(string.ascii_uppercase, 4))
            room = Room(
                id=code,
                last_activation=int(
                    time.time() - app.config["ACTIVATION_RESET_MS"] / 1000
                ),
                placement=0,
            )
            db.session.add(room)
            db.session.commit()
            log.info(f"Created new room: {code}")
            break
        except Exception as e:
            log.error(e)
            code = None
    return code
