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
##list:
0.Exit - you can exit the program by selecting 0 
1.Create New Events:  Easily create events by providing event details like name, date, location, and description.
2.List Events: View a list of all created events.
3.Add Attendees: Assign attendees to specific events by providing attendee details (name and email).
4.Delete Events: Remove events that are no longer needed.
5.Find Event by Name: Quickly search for events by name.
6.View Attendees for an Event: List all attendees for a specific event.

**Extensive  FEATURES Guide**
**Option 1**:
Create a New Event

    Select option 1 in the menu.
        You will be prompted to enter the following details:
            Event Name: A name for the event.
            Event Date: The date of the event.
                - this can be in whatever format you prefer as it takes in text as is. 10/01/2024 , 2024-10-01, October 01, 2024. etc.
            Event Location: The location where the event will take place.
                - please provie the name of the location the event is held
            Event Description: A description of the event.
                - Provide a decription of the event details. What is the event for? (in my case here I would put details of the songs i sang and any outstanding points of interest that may pertain to me or the experience.)
        Once completed, you’ll see a message confirming the event has been created.

**Option 2**
List All Events

    Select option 2 in the menu.
        This option allows you to view all existing events:
            You will see a table listing all events, including:
                ID: The unique ID of the event.
            Name: The name of the event.
            Date: The event date.
            Location: Where the event will take place.
            Description: A brief description of the event.
            Attendees: A list of attendees registered for the event.

**Option 3**
Add an Attendee to an Event

    Select option 3.
        This option lets you add attendees to an event:
            You will be prompted to:
                Enter the Event ID: The ID of the event you want to add the attendee to.
                Enter Attendee Name: The name of the attendee.
                Enter Attendee Email: The email address of the attendee.

You will receive a confirmation message that the attendee has been added to the Event. 

**Option 4**
Delete an Event

Select option 4.
    You can delete an event by selecting this option.
        Enter the Event ID of the event you wish to delete.
        If the event exists, it will be deleted, and you’ll see a confirmation of it's deletion.

**Option 5**
Find an Event by Name

    Select option 5.
        You can search for events by name:
            Enter the Event Name you want to search for.
            If matching events are found, they will be displayed.

**Option 6**
List Attendees for an Event
    Select Option 6:
        You can view all attendees for a specific event:
            Enter the Event ID to view the attendees for that event.
            If attendees are found, they will be listed in a table that includes their:
                ID: The attendee's unique ID.
                Name: The name of the attendee.
                Email: The email address of the attendee.

**Option 7**
Delete an Attendee
Select Option 7
    You can delete an attendee by selecting this option:
        Enter the Attendee ID of the attendee you wish to delete.
        If the attendee exists, they will be deleted, and you’ll see:

**Troubleshooting**
Common Errors:
Event Not Found: If you try to find or delete an event that doesn’t exist, you’ll see a message like:


Event not found.
Attendee Not Found: Similarly, if you try to find or delete an attendee that doesn’t exist, you’ll see:


Attendee not found.
Resetting the Database:
If you need to reset the database (for example, during testing), you can use the drop_table method for both Event and Attendee:



