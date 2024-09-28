from .. import CURSOR, CONN
 

class Event:
    all = {}
    
    def __init__(self, name, date, location, description, id=None):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.description = description
    
    def __repr__(self):
        return f"<Event {self.id}: {self.name}, {self.date}, {self.location}>"
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name
        else:
            raise ValueError(" Name Must be a string longer than 0 characters")
    
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date.strip()) > 0:
            self._date = date
        else:
            raise ValueError("Date Must be a string longer than 0 characters")
    
    
    @property
    def location(self):
        return self._location 
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location.strip()) > 0:
            self._location = location
        else:
            raise ValueError("Must be a string longer than 0 characters")
    
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description.strip()) > 0:
            self._description = description
        else:
            raise ValueError("Must be a string longer than 0 characters")

    
    @classmethod
    def create_table(cls): 
        """create an events table if it DOESNT exist"""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                name TEXT,
                date TEXT,
                location TEXT,
                description TEXT
            )
        ''')
        """always commit changes after executing a SQL statement"""
        CONN.commit()
    
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS events')
        CONN.commit()
    def save(self):
        if self.id is None:
            CURSOR.execute('''
                INSERT INTO events (name, date, location, description)
                VALUES(?, ?, ?, ?)
            ''', (self.name, self.date, self.location, self.description))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute('''
                UPDATE events
                SET name = ?, date = ?, location = ?, description = ?
                WHERE id = ?
            ''', (self.name, self.date, self.location, self.description, self.id,))
            CONN.commit()
        type(self).all[self.id] = self    
    
    def delete(self):
        if self.id is not None:
            CURSOR.execute('DELETE FROM events WHERE id = ?', (self.id,))
            CONN.commit()
            if self.id in type(self).all:
                del type(self).all[self.id]
            self.id = None
        else:
            raise ValueError("Event does not exist in the database")
    
    
    @classmethod
    def get_all(cls):
        rows = CURSOR.execute('SELECT * FROM events').fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    
    @classmethod
    def find_by_id(cls, event_id):
        row = CURSOR.execute('SELECT * FROM events WHERE id = ?', (event_id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    
    
    @classmethod
    def instance_from_db(cls, row):
        event_id = row[0]
        if event_id in cls.all:
            return cls.all[event_id]
        event = cls(id=row[0], name=row[1], date=row[2], location=row[3], description=row[4])
        cls.all[event.id] = event
        return event
    
    
    @classmethod
    def create(cls, name, date, location, description):
        event = cls(name, date, location, description)
        event.save()
        return event
    