from lib.models.event import Event
from lib.models.attendee import Attendee
from lib.models.venue import Venue
from lib import commit_and_close
from lib import CURSOR, CONN

def enable_foreign_keys():
    CURSOR.execute("PRAGMA foreign_keys = ON;")
    CONN.commit()

def setup_database():
    Attendee.create_table()
    Event.create_table()
    Venue.create_table()
    

if __name__ == "__main__":
    setup_database()
    print("DataBase Setup has been Completed!")
    commit_and_close()