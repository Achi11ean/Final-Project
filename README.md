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

**FEATURES Quick Overview**
0. Exit: Exit the program.
1. Create a New Venue: Create a venue for events.
2. Create a New Event: Create events by providing event details like name, date, location, and description.
3. Add an Attendee: Add a new attendee to an event by providing their name and email.
4. Add an Existing Attendee to an Event: Assign an attendee who has already been created to another event.
5. Add an Existing Venue to an Event: Assign a venue to an existing event.
6. List All Venues: View a list of all created venues.
7. List All Events: View a list of all created events.
8. View Attendees for an Event: List all attendees for a specific event.
9. List All Attendees: View a list of all attendees in the database.
10. Search Events by Venue: Search and list events taking place at a specific venue.
11. Find Event by Name: Quickly search for events by name.
12. Delete a Venue: Remove a venue that is no longer needed.
13. Delete an Event: Remove events that are no longer needed.
14. Delete an Attendee: Remove attendees from the system.
15. Remove an Attendee from an Event: Unassign an attendee from a specific event without deleting the attendee.
**FEATURES GUIDE EXPANDED**
# Option 1:
Create a New Venue
Select option 1 in the menu.
You will be prompted to enter:
1. Venue Name: The name of the venue.
2. Event Organizer: The name of the person organizing the event.
3. Venue Earnings: The total earnings for the venue.
A confirmation message will indicate that the venue has been created.
# Option 2:
Create a New Event
Select option 2 in the menu.
You will be prompted to enter:
1. Event Name: The name of the event.
2. Event Date: The date of the event.
3. Event Location: The venue where the event will take place.
4. Event Description: A description of the event.
5. A confirmation message will indicate that the event has been created.
# Option 3:
Add an Attendee to an Event
Select option 3 in the menu.
You will be prompted to enter:
1. Event ID: The ID of the event.
2. Attendee Name: The name of the attendee.
3. Attendee Email: The email of the attendee.
4. A confirmation message will indicate that the attendee has been added to the event.
# Option 4: 
Add an Existing Attendee to an Event
Select option 4 in the menu.
You can assign an attendee already in the system to another event by:
1. Selecting the Event ID.
2. Selecting the Attendee ID.
# Option 5: 
Add an Existing Venue to an Event
Select option 5 in the menu.
You can assign an existing venue to an event by:
1. Selecting the Event ID.
2. Selecting the Venue ID.
A confirmation message will indicate that the venue has been assigned to the event.
# Option 6: 
List All Venues
Select option 6 to view a list of all venues.
The table will show the following details:
1. ID: The unique ID of the venue.
2. Name: The name of the venue.
3. Organizer: The event organizer.
4. Earnings: The venue's earnings.
# Option 7: 
List All Events
Select option 7 to view a list of all events.
The table will display details for each event, including the attendees.
# Option 8: 
List Attendees for an Event
Select option 8 to view all attendees for a specific event.
You will be prompted to provide the Event ID, and if there are attendees, they will be listed in a table.
# Option 9: 
List All Attendees
Select option 9 to view a list of all attendees in the database.
The table will show each attendee's ID, name, and email.
# Option 10: 
Search Events by Venue
Select option 10 to search for events at a specific venue.
Provide the Venue ID, and all events associated with that venue will be listed.
# Option 11: 
Find an Event by Name
Select option 11 to search for an event by its name.
Matching events will be displayed in a table.
# Option 12: 
Delete a Venue
Select option 12 to delete a venue.
Provide the Venue ID, and the venue will be deleted if it exists.
# Option 13: 
Delete an Event
Select option 13 to delete an event.
Provide the Event ID, and the event will be deleted if it exists.
# Option 14: 
Delete an Attendee
Select option 14 to delete an attendee from the system.
Provide the Attendee ID, and the attendee will be deleted if they exist.
# Option 15: 
Remove an Attendee from an Event
Select option 15 to remove an attendee from a specific event.
Provide the Event ID and Attendee ID, and the attendee will be unassigned from the event.

                                            ### Troubleshooting  ###
**Event Not Found:** If you try to find or delete an event that doesn’t exist, you’ll see a message like Event not found.

**Attendee Not Found:** If you try to find or delete an attendee that doesn’t exist, you’ll see a message like Attendee not found.

**Venue Not Found:** If you try to find or delete a venue that doesn’t exist, you’ll see a message like Venue not found.

# Resetting the Database
If you need to reset the database (e.g., during testing), use the drop_table method for both the Event and Attendee models.