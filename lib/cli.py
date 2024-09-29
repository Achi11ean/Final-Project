# lib/cli.py
#importing all classes necessary
from .models.event import Event
from .models.attendee import Attendee
from rich.console import Console
from rich.table import Table

#initialize the Rich console for styled outputs
console = Console()

#Function to exit the program with a print to confirm program exiting. 
def exit_program():
    console.print("[bold red]Exiting the program[/bold red]")
    exit()

#Function to create a new event with a prompt for the user to enter the event details.
def create_event():
    name = input("Enter Event Name: ")
    date = input("Enter Event Date: ")
    location = input("Enter Event Location: ")
    description = input("Enter Event Description: ")
    #create a new event using the event model
    event = Event.create(name, date, location, description)
    #Print confirmation fro event
    console.print(f"[green]Event Created:[/green] {event}")

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
        #Loop through each event and display its details in the table
        for event in events:
            attendees = Attendee.find_by_event_id(event.id) #find all attendees for the current event
            attendees_str = ", ". join([attendee.name for attendee in attendees]) if attendees else "No Attendees, sorry!" #create a string of attendee names or a message if no attendees are found 
            table.add_row(str(event.id), event.name, event.date, event.location, event.description, attendees_str) #add a row to the table for each event
            
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
        attendee = Attendee.create(name, email, event.id)
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
def find_by_event_name():
    name = input("Enter event name to search: ")
    events = Event.get_all()
    matching_events = [event for event in events if event.name == name]
    if matching_events:
        for event in matching_events:
            print(event)
    else:
        console.print("[yellow]No event found with that name.[/yellow]")


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
            table.add_column("Event ID", justify="right", style="blue")
        
            for attendee in attendees:
                table.add_row(
                    str(attendee.id),
                    attendee.name,
                    attendee.email,
                    str(attendee.event_id)
                )
            console.print(table)
        else:
            console.print("[yellow]No attendees found for this event.[/yellow]")
    else:
        console.print("[yellow]Event Not found[/yellow]")
#main function that runs CLI loop - 
def main():
    while True:     #infinite loop to keep the program running
        menu()
        choice = input("> ") #get user's choice
        if choice == "0":       #match users input to an action
           exit_program()
        elif choice == "1":
            create_event()
        elif choice == "2":
            list_events()
        elif choice == "3":
            add_attendee()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            find_by_event_name()
        elif choice == "6":
            list_event_attendees()
        elif choice == "7":
            delete_attendee()
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")

#function to display menu 
def menu():
    console.print(f"[bold green underline]Please select an option:[/bold green underline]")
    console.print("[bold red]0. Exit the program[/bold red]")
    console.print("[blue]1. Create a New Event[/blue]")
    console.print("[blue]2. List All Events[/blue]")
    console.print("[blue]3. Add An Attendee to an Event![/blue]")
    console.print("[yellow]4. Delete an event[/yellow]")
    console.print("[blue]5. Find an event by name[/blue]")
    console.print("[blue]6. List Attendees for an Event[/blue]")
    console.print("[yellow]7. Delete and attendee[/yellow]")

if __name__ == "__main__":
    main()
