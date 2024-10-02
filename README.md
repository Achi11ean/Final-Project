# Event Planner Command-Line-Interface Application!

##Overview

The **Event Planner** is a Python-based command-line interface application designed to help users manage events and attendees.
I personally created this to track my singing performances and friends and family that helped support me along the way!

The application allows users to create events, add attendees, view all events, and manage attendees for a specific event. (i.e. delete attendees)
                    All through the terminal!
                    
                        
## Installation

To use the Event Planner CLI, you need Python installed on your machine. Follow these steps:

1. Clone this repository:
    git clone https://github.com/your-username/event-planner-cli.git

2. Navigate to the project directory:
    FINAL-PROJECT

3. OPEN TERMINAL:
    with your terminal open confirm you have the latest versions of the systems necessary to operate installed. you will need the following:
    Python: test you have this by running|| python --version
    pipenv --version 
    Sql extension for VS code. (this is an extension in VS code you can add)


4. Next in your terminal run ' pip install rich ' 
This will set a prompt pop up asking to set this up in a virtual environment, click confirm to allow this.

5. Now that we have everything installed and set up enter the following into the command:

    python -m lib.main

after that runs and creates the database you can now open up the event planner with:

    python -m lib.cli

## Using the Event Planner: A Guide.

After installation, you can run the application by following these steps:

**FEATURES Quick Overview!**
0. Exit - Exit the program.
1. Create a New Venue - Easily create a venue for events.
2. Create a New Event - Provide event details like name, date, location, and description.
3. Add Attendees - Assign attendees to specific events by providing attendee details (name and email).
4. Add an Existing Attendee to an Event - Add an attendee who has already been created to an existing event.
5. List All Venues - View a list of all created venues.
6. List All Events - View a list of all created events.
7. View Attendees for an Event - List all attendees for a specific event.
8. Search Events by Venue - Search and list events taking place at a specific venue.
9. Find Event by Name - Quickly search for events by name.
10. Delete a Venue - Remove a venue that is no longer needed.
11. Delete an Event - Remove events that are no longer needed.
12. Delete an Attendee - Remove attendees from the system.
**FEATURES GUIDE EXPANDED**
Extensive FEATURES Guide
**Option 1:**
Create a New Venue
Select option 1 in the menu.
You will be prompted to enter the following details:

1. A name for the venue.
2.Event Organizer: Name of the person organizing events at this venue.
3.Venue Earnings: Earnings for the venue.
Once completed, you’ll see a confirmation message that the venue has been created.

**Option 2:**
Create a New Event
Select option 2 in the menu.
You will be prompted to enter the following details:

1.Event Name: A name for the event.
2.Event Date: The date of the event.
3.Event Location: The location (Venue) where the event will take place.
4.Event Description: A description of the event.
Once completed, you’ll see a confirmation that the event has been created.

**Option 3:**
Add an Attendee to an Event
Select option 3 in the menu.
This option lets you add attendees to an event. You will be prompted to:

1.Enter the Event ID: The ID of the event to add the attendee to.
2.Enter Attendee Name: The name of the attendee.
3.Enter Attendee Email: The email address of the attendee.
A confirmation message will show that the attendee has been added to the event.

**Option 4:**
Add an Existing Attendee to an Event
Select option 4 in the menu.
This option allows you to add an attendee that already exists in the system to another event:

1.Select the Event ID for the event.
2.Select the Attendee ID to associate the attendee with the event.

**Option 5:**
List All Venues
Select option 5 to view all venues:

You will see a table listing each venue, including:
ID: The unique ID of the venue.
Name: The venue name.
Organizer: Name of the event organizer.
Earnings: Venue earnings.

**Option 6:**
List All Events
Select option 6 to view all existing events.
A table will list each event and its details, including the attendees registered for the event.

**Option 7:**
List Attendees for an Event
Select option 7 to view all attendees for a specific event.
You will need to provide the Event ID, and if there are attendees, they will be listed in a table.

**Option 8:**
Search Events by Venue
Select option 8 to search for events by venue.
You will need to provide the Venue ID, and all events held at that venue will be displayed.

**Option 9:**
Find an Event by Name
Select option 9 to search for an event by name.
If matching events are found, they will be displayed in a table.

**Option 10:**
Delete a Venue
Select option 10 to delete a venue.
Provide the Venue ID, and the venue will be deleted if it exists.

**Option 11:**
Delete an Event
Select option 11 to delete an event.
Provide the Event ID, and the event will be deleted if it exists.

**Option 12:**
Delete an Attendee
Select option 12 to delete an attendee.
Provide the Attendee ID, and the attendee will be deleted if it exists.

**Troubleshooting**
Common Errors:

Event Not Found: If you try to find or delete an event that doesn’t exist, you’ll see a message like:
Event not found.

Attendee Not Found: Similarly, if you try to find or delete an attendee that doesn’t exist, you’ll see:
Attendee not found.

Resetting the Database: If you need to reset the database (for example, during testing), you can use the drop_table method for both Event and Attendee.

