# lib/cli.py
#importing all classes necessary
from .models.event import Event
from .models.attendee import Attendee
from .models.venue import Venue
from rich.console import Console
from rich.table import Table

#initialize the Rich console for styled outputs
console = Console()

#Function to exit the program with a print to confirm program exiting. 
def exit_program():
    console.print("[bold red]Exiting the program[/bold red]")
    exit()

#Function to create a new event with a prompt for the user to enter the event details.
def validate_integer_input(prompt):
    """Prompts the user for an integer input and retries if not valid."""
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            return int(user_input)
        console.print("[red]Invalid input. Please enter a valid integer.[/red]")

def create_event():
    name = input("Enter Event Name: ").strip()
    date = input("Enter Event Date: ").strip()
    location = input("Enter Event Location: ").strip()
    description = input("Enter Event Description: ").strip()
    # Select Venue for the Event
    venues = Venue.get_all()
    if venues:
        console.print("[blue] Available Venues: [/blue]")
        for venue in venues:
            console.print(f"ID: {venue.id}, Name: {venue.name}")
        # Using integer validation for venue ID
        venue_id = validate_integer_input("Enter Venue ID for This Event: ")
        venue = Venue.find_by_id(venue_id)
        if not venue:
            console.print("[yellow]Invalid Venue ID. Please try again.[/yellow]")
            return
    else:
        console.print("[yellow]No available Venues. Please create a venue first.[/yellow]")
        return
    # Create the event using the event model
    event = Event.create(name, date, location, description, venue_id)
    # Allow selecting existing attendees for this new event
    attendees = Attendee.get_all()
    if attendees:
        console.print("[blue]Available Attendees: [/blue]")
        for attendee in attendees:
            console.print(f"ID: {attendee.id}, Name: {attendee.name}, Email: {attendee.email}")
        attendee_ids = input("Enter comma-separated Attendee IDs to add to this event (or leave blank to skip): ").split(',')
        attendee_ids = [attendee_id.strip() for attendee_id in attendee_ids if attendee_id.strip().isdigit()]
        # Add selected attendees to the event
        if attendee_ids:
            for attendee_id in attendee_ids:
                attendee = Attendee.find_by_id(attendee_id)
                if attendee:
                    attendee.add_to_event(event.id)
                    console.print(f"[green]Attendee {attendee.name} added to event {event.name}.[/green]")
                else:
                    console.print(f"[yellow]Attendee with ID {attendee_id} not found.[/yellow]")
        else:
            console.print("[yellow]No attendees selected for this event.[/yellow]")
    else:
        console.print("[yellow]No existing attendees found. You can add attendees later.[/yellow]")

    console.print(f"[green]Event Created: {event}[/green]")
    #function to list all events 
def list_events():
    #Fetch all events from the DB 
    events = Event.get_all()
    if events: #Check if there are any events
        #Create a table with styled columns to display the event details
        table = Table(title="[bold red]Events List[/bold red ]")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Date", justify="center", style="green")
        table.add_column("Location", style="blue")
        table.add_column("Description", style="magenta")
        table.add_column("Attendees", style="yellow")
        table.add_column("Venue ID", style="blue")
        #Loop through each event and display its details in the table
        for event in events:
            attendees = Attendee.find_by_event_id(event.id) #find all attendees for the current event
            attendees_str = ", ". join([attendee.name for attendee in attendees]) if attendees else "No Attendees, sorry!" #create a string of attendee names or a message if no attendees are found 
            table.add_row(str(event.id), event.name, event.date, event.location, event.description, attendees_str, str(event.venue_id)) #add a row to the table for each event
            
        console.print(table)#display table in the console
    else:
        console.print("[yellow]No events found.[/yellow]")#if no events are found display error message.

        #function to add an attendee to an event with a prompt to the user to enter attendee and event details. 
def add_attendee():
    event_id = input("Enter the event ID: ")
    name= input("Enter attendee name: ")
    email = input("Enter attendee Email: ")
    #find the event by ID
    event = Event.find_by_id(event_id)
    if event:
        #if event is found create a new attendee for the event and print it to the console. if not found raise an error for the user to know. 
        attendee = Attendee.create(name, email)
        attendee.add_to_event(event.id)
        console.print(f"[green ]Attendee {attendee} added to the event {event.name}.[/green]")
    else: 
        console.print("[yellow]Event not found.[/yellow]")

        #function to delete an attendee with a promt for attendee ID. if attendee exists, delete it and confirm it's deletion. If it's doesn't exist, raise an error. 
def delete_attendee():
    attendee_id = input("Enter the Attendee ID to delete: ")
    attendee = Attendee.find_by_id(attendee_id)
    if attendee:
        attendee.delete()
        console.print(f"[red] Attendee {attendee.name} has been deleted.[/red]")
    else:
        console.print("[yellow]Attendee Not found. [/yellow]")
def add_attendee_to_event():
    attendee_id = input("Enter the attendee ID: ")
    event_id = input("Enter the event ID: ")
    
    attendee = Attendee.find_by_id(attendee_id)
    if attendee:
        attendee.add_to_event(event_id)
        console.print(f"[green]Attendee {attendee.name} added to event ID {event_id}.[/green]")
    else:
        console.print("[yellow]Attendee not found.[/yellow]")
        
        #function to delete an event with a prompt for the event ID to delete a specified event. if it exists, show a confirmation it's deleted. if not raise a user error.
def delete_event():
    event_id = input("Enter Event ID to delete: ")
    event = Event.find_by_id(event_id)
    if event:
        event.delete()
        console.print(f"[red]Event {event.name} deleted.[/red]")
    else:
        console.print("[yellow]Event not found[/yellow]")

    #function to find an event by name prompting a user enter the event name. 
    # Then get all of the events from the database and find any matching the entry. if they match, display it. if not display a warning
# Function to find an event by name and display in a table
def find_by_event_name():
    name = input("Enter event name to search: ").strip()
    events = Event.get_all()
    matching_events = [event for event in events if name.lower() in event.name.lower()]

    if matching_events:
        # Create a table with styled columns to display the matching events
        table = Table(title=f"[bold green]Events Matching: '{name}'[/bold green]")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Date", style="green")
        table.add_column("Location", style="blue")
        table.add_column("Description", style="magenta")
        table.add_column("Attendees", style="yellow")
        table.add_column("Venue ID", style="blue")

        # Loop through matching events and display them in the table
        for event in matching_events:
            attendees = Attendee.find_by_event_id(event.id)
            attendees_str = ", ".join([attendee.name for attendee in attendees]) if attendees else "No Attendees"
            table.add_row(
                str(event.id), event.name, event.date, event.location, event.description, attendees_str, str(event.venue_id))

        console.print(table)
    else:
        console.print(f"[yellow]No event found with the name '{name}'.[/yellow]")

#function to list all attendees for a specific event. user enters ID. fin the event by that ID and if attendees found create a table to display the details - adding a row for each attendee
def list_event_attendees():
    event_id = input("Enter the event ID:")
    event = Event.find_by_id(event_id)
    if event:
        attendees = Attendee.find_by_event_id(event.id)
        if attendees:
            table = Table(title=f"[bold green]Attendees for Event: {event.name}[/bold green]")

            table.add_column("ID", justify="right", style="cyan", no_wrap=True)
            table.add_column("Name", style="magenta")
            table.add_column("Email", style="yellow")
        
            for attendee in attendees:
                table.add_row(str(attendee.id), attendee.name, attendee.email)
            console.print(table)
        else:
            console.print("[yellow]No attendees found for this event.[/yellow]")
    else:
        console.print("[yellow]Event Not found[/yellow]")

def add_existing_attendee_to_event():
    # List all events to select from
    events = Event.get_all()
    if not events:
        console.print("[yellow]No events found.[/yellow]")
        return
    
    console.print("[blue]Available Events:[/blue]")
    for event in events:
        console.print(f"ID: {event.id}, Name: {event.name}")
    
    # Get event ID from the user
    event_id = validate_integer_input("Enter the Event ID to add the attendee to: ")
    event = Event.find_by_id(event_id)
    
    if not event:
        console.print("[red]Event not found.[/red]")
        return

    # List all attendees to select from
    attendees = Attendee.get_all()
    if not attendees:
        console.print("[yellow]No attendees found.[/yellow]")
        return
    
    console.print("[blue]Available Attendees:[/blue]")
    for attendee in attendees:
        console.print(f"ID: {attendee.id}, Name: {attendee.name}, Email: {attendee.email}")
    
    # Get attendee ID from the user
    attendee_id = validate_integer_input("Enter the Attendee ID to add to the event: ")
    attendee = Attendee.find_by_id(attendee_id)
    
    if not attendee:
        console.print("[red]Attendee not found.[/red]")
        return
    try:
    # Add the attendee to the event
        attendee.add_to_event(event.id)
        console.print(f"[green]Attendee {attendee.name} added to event {event.name}.[/green]")
    except ValueError as e:
        console.print(f"[yellow]{str(e)}[/yellow]")

def search_venue_events():
    venue_id = input("Enter Venue ID to Search for Events: ")
    venue = Venue.find_by_id(venue_id)
    if venue:
        events = Venue.find_events_by_venue_id(venue.id)
        if events:
            console.print(f"[green] Events for Venue {venue.name}: [/green]")
            table = Table(title=f"Events at {venue.name}")
            table.add_column("ID", justify="right", style="cyan", no_wrap=True)
            table.add_column("Name", style="magenta")
            table.add_column("Date", style="green")
            table.add_column("Location", style="blue")
            table.add_column("Description", style="yellow")
            for event in events:
                table.add_row(str(event.id), event.name, event.date, event.location, event.description)
            
            console.print(table)
        else:
            console.print("[yellow]No Events Found for this Venue.[/yellow]")
    else:
        console.print("[red]Venue not found.[/red]")
    
def list_venues():
    venues = Venue.get_all()
    if venues:
        table = Table(title="[bold blue] Venues List [/bold blue]")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Organizer", style="yellow")
        table.add_column("Earnings", style="green")
        for venue in venues:
            table.add_row(str(venue.id), venue.name, venue.organizer, str(venue.earnings))
        console.print(table)
    else:
        console.print("[yellow] No Venues Found.")

def create_venue():
    name = input("Enter Venue Name: ")
    organizer = input("Enter Event Organizer Name: ")
    earnings = input("Enter Venue Earnings: ")
    venue = Venue.create(name=name, organizer=organizer, earnings=earnings)
    console.print(f"[green]Venue Created:[/green] {venue}")

def delete_venue():
    venue_id = input("Enter Venue ID to delete: ")
    venue = Venue.find_by_id(venue_id)
    if venue:
        venue.delete()
        console.print(f"[red]Venue {venue.name} deleted.[/red]")
    else:
        console.print("[yellow]Venue not found[/yellow]")

#main function that runs CLI loop - 
def main():
    while True:     # Infinite loop to keep the program running
        menu()
        choice = input("> ") # Get user's choice
        
        # Grouped Create Operations
        if choice == "0":       # Exit the program
           exit_program()
        elif choice == "1":     # Create a new venue
            create_venue()
        elif choice == "2":     # Create a new event
            create_event()
        elif choice == "3":     # Add an attendee to an event
            add_attendee()
        elif choice == "4":     # Add an existing attendee to an existing event
            add_existing_attendee_to_event()
        
        # Grouped List Operations
        elif choice == "5":     # List all venues
            list_venues()
        elif choice == "6":     # List all events
            list_events()
        elif choice == "7":     # List attendees for an event
            list_event_attendees()
        elif choice == "8":     # Search events by venue
            search_venue_events()
        elif choice == "9":    # Find an event by name
            find_by_event_name()
            
        # Grouped Delete Operations
        elif choice == "10":     # Delete a venue
            delete_venue()
        elif choice == "11":     # Delete an event
            delete_event()
        elif choice == "12":    # Delete an attendee
            delete_attendee()
        # Invalid input handling
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
#function to display menu 
def menu():
    console.print(f"[bold green underline]Please select an option:[/bold green underline]")
    
    # Grouped Create Options
    console.print("[bold blue]1. Create A New Venue[/bold blue]")
    console.print("[bold blue]2. Create A New Event[/bold blue]")
    console.print("[bold blue]3. Add An Attendee to an Event[/bold blue]")
    console.print("[bold blue]4. Add An Existing Attendee to an Existing Event")
    
    # Grouped List Options
    console.print("[bold blue]5. List All Venues[/bold blue]")
    console.print("[bold blue]6. List All Events[/bold blue]")
    console.print("[bold blue]7. List Attendees for an Event[/bold blue]")
    console.print("[bold blue]8. Search Events by Venue[/bold blue]")
    console.print("[bold blue]9. Find An Event by Name[/bold blue]")
    
    # Grouped Delete Options
    console.print("[bold yellow]10. Delete A Venue[/bold yellow]")
    console.print("[bold yellow]11. Delete An Event[/bold yellow]")
    console.print("[bold yellow]12. Delete An Attendee[/bold yellow]")
    
    # Miscellaneous Option

    
    # Exit Option
    console.print("[bold red]0. Exit The Program[/bold red]")
if __name__ == "__main__":
    main()
