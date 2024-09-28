# Event Planner Command-Line-Interface Application!

##Overview

The **Event Planner** is a Python-based command-line interface application designed to help users manage events and attendees.

The application allows users to create events, add attendees, view all events, and manage attendees for a specific event. 
                    All through the terminal!
                    
                        
**FEATURES!**
##list:
0.Exit - you can exit the program by selecting 0 
1.Create New Events:  Easily create events by providing event details like name, date, location, and description.
2.List Events: View a list of all created events.
3.Add Attendees: Assign attendees to specific events by providing attendee details (name and email).
4.Delete Events: Remove events that are no longer needed.
5.Find Event by Name: Quickly search for events by name.
6.View Attendees for an Event: List all attendees for a specific event.

## Installation

To use the Event Planner CLI, you need Python installed on your machine. Follow these steps:

1. Clone this repository:
    git clone https://github.com/your-username/event-planner-cli.git

2. Navigate to the project directory:
    cd event-planner-cli

3. Create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

4. Install dependencies:
    Make sure you have a `Pipfile` in your project, and then install the dependencies using:
    

## Usage

After installation, you can run the application by following these steps:

1. **Set Up the Database**:
   Initialize the database and create the required tables by running:
   python -m lib.main
2. Open Database for use:  
   python -m lib.cli