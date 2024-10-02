from .. import CURSOR, CONN

class Attendee:
    #This Class represents an Attendee and manages the DB interactions for the attendees table


    #This is a dictionary to keep track of all attendee objects in memory
    all = {}
    #initialize an Attendee object with name, email, and an optional id 
    #If  the object is new Id is None and is automatically generated when saving to the DB
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email
            
    #String Representation of the attendee object.
    def __repr__(self):
        return f"<Attendee {self.id}: {self.name}, {self.email}>"

    #Property Methods for name, email, event_ id with validationssss 
    #Getter for the attendee's name
    @property
    def name(self):
        return self._name
    
    #Setter for the attendee's name with validation to make sure it is a NONEMPTY STRING
    @name.setter
    def name(self, name):
        if isinstance(name,str) and len(name.strip()) > 0:
            self._name = name
        else: 
            raise ValueError("Name must be a string longer than 0 Characters")
    
    #Getter for the attendee's email
    @property
    def email(self):
        return self._email
    
    #setter for the attendee's email with validation to ensure email contains @ and . for basic email validation
    @email.setter
    def email(self,email):
        if "@" in email and "." in email:
            self._email = email
        else:
            raise ValueError("Please Enter a valid email")

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS attendees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        ''')
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS attendee_events (
                attendee_id INTEGER,
                event_id INTEGER,
                FOREIGN KEY (attendee_id) REFERENCES attendees(id) ON DELETE CASCADE,
                FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
                PRIMARY KEY (attendee_id, event_id)
            )
        ''')
        CONN.commit()
    @classmethod
    def drop_table(cls):
        #Drop the attendees table from the database useful during testing to reset the DB
        CURSOR.execute('DROP TABLE IF EXISTS attendees')
        CONN.commit()
    def save(self):
        #save the attendee object to the DB, if the attendee is new (id = None) it will be inserted into the table. Otherwise an existin one will be updated.
        if self.id == None:
            #insert a new row into the attendee's table
            CURSOR.execute('''
                INSERT INTO attendees(name, email)
                VALUES (?, ?)
            ''', (self.name, self.email))
            CONN.commit()
            #set the id of the object to the last inserted row's id
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
        else:
            #update the existing row with new values
            CURSOR.execute('''
                UPDATE attendees
                SET name = ?, email = ?
                WHERE id = ?
            ''', (self.name, self.email, self.id))
            CONN.commit()
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        #factory method to create a new attendee object and save it to the DB
        attendee = cls(name, email)
        attendee.save()
        return attendee
    def delete(self):
        #delete the attendee object from the DB; removes the record from the attendees table and from the in-memory dictionary
        if self.id is not None:
            #delete the row from the table
            CURSOR.execute('DELETE FROM attendees WHERE id= ?', (self.id,))
            CONN.commit()
            #remove the object from the in-memory dictionary
            del type(self).all[self.id]
            self.id = None
        else:
            raise ValueError("Attendee does not exist in the database")
    @classmethod
    def get_all(cls):
        #fetch all attendee records from the DB and return them as a list of attendee objects
        rows = CURSOR.execute("SELECT * FROM attendees").fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls, attendee_id):
        #find an attendee by their unique ID if found return the attendee object; otherwise return None
        row = CURSOR.execute("SELECT * FROM attendees WHERE id = ?", (attendee_id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    @classmethod
    def find_by_event_id(cls, event_id):
        # This method will retrieve attendees by event_id from the attendee_events association table
        rows = CURSOR.execute('''
            SELECT attendees.* FROM attendees
            JOIN attendee_events ON attendees.id = attendee_events.attendee_id
            WHERE attendee_events.event_id = ?
        ''', (event_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        #return an attendee object initialized from a DB row, the row is expected to contain the ID, name, email and event_id,
        attendee_id = row[0]
        #check if the attendee already exists in memory to avoid duplication
        if attendee_id in cls.all:
            return cls.all[attendee_id]
        #create a new attendee object and add it to the in memory dictionary
        attendee = cls(id=row[0], name=row[1], email=row[2])
        cls.all[attendee.id] = attendee
        return attendee
    
    def add_to_event(self, event_id):
    # Check if the attendee is already associated with the event
        existing_record = CURSOR.execute('''
            SELECT * FROM attendee_events 
            WHERE attendee_id = ? AND event_id = ?
        ''', (self.id, event_id)).fetchone()

        if existing_record:
            raise ValueError(f"Attendee {self.name} is already added to this event.")
    # If not already associated, insert into the attendee_events table
        CURSOR.execute('''
            INSERT INTO attendee_events (attendee_id, event_id)
            VALUES (?, ?)
        ''', (self.id, event_id))
        CONN.commit()

    @classmethod
    def get_events_for_attendee(cls, attendee_id):
        rows = CURSOR.execute('''
            SELECT events.* FROM events
            JOIN attendee_events ON events.id = attendee_events.event_id
            WHERE attendee_events.attendee_id = ?
        ''', (attendee_id,)).fetchall()
        from .event import Event
        return [Event.instance_from_db(row) for row in rows]


