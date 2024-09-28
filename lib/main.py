from lib.models.event import Event
from lib.models.attendee import Attendee
from lib import commit_and_close

def setup_database():
    """create tables for event and attendee models."""
    Event.create_table()
    Attendee.create_table()

if __name__ == "__main__":
    setup_database()
    print("DataBase Setup has been Completed!")
    commit_and_close()