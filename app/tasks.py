from app.room import clear_rooms

from app import app, scheduler


@scheduler.task("interval", id="cleanup-job", minutes=3)
def cleanup():
    clear_rooms(app.config["INACTIVITY_THRESHOLD_SEC"])
