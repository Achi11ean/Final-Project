# lib/cli.py

from .models.event import Event
from .models.attendee import Attendee
from rich.console import Console
from rich.table import Table

console = Console()
def exit_program():
    console.print("[bold red]Exiting the program[/bold red]")
    exit()
def create_event():
    name = input("Enter Event Name: ")
    date = input("Enter Event Date: ")
    location = input("Enter Event Location: ")
    description = input("Enter Event Description: ")

    event = Event.create(name, date, location, description)
    console.print(f"[green]Event Created:[/green] {event}")
def list_events():
    events = Event.get_all()
    if events: 
        table = Table(title="[bold red]Events List[/bold red ]")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Date", justify="center", style="green")
        table.add_column("Location", style="blue")
        table.add_column("Description", style="magenta")
        table.add_column("Attendees", style="yellow")
        for event in events:
            attendees = Attendee.find_by_event_id(event.id)
            attendees_str = ", ". join([attendee.name for attendee in attendees]) if attendees else "No Attendees, sorry!"
            table.add_row(str(event.id), event.name, event.date, event.location, event.description, attendees_str)
            
        console.print(table)
    else:
        console.print("[yellow]No events found.[/yellow]")
def add_attendee():
    event_id = input("Enter the event ID: ")
    name= input("Enter attendee name: ")
    email = input("Enter attendee Email: ")

    event = Event.find_by_id(event_id)
    if event:
        attendee = Attendee.create(name, email, event.id)
        console.print(f"[green ]Attendee {attendee} added to the event {event.name}.[/green]")
    else: 
        console.print("[yellow]Event not found.[/yellow]")
def delete_attendee():
    attendee_id = input("Enter the Attendee ID to delete: ")
    attendee = Attendee.find_by_id(attendee_id)
    if attendee:
        attendee.delete()
        console.print(f"[red] Attendee {attendee.name} has been deleted.[/red]")
    else:
        console.print("[yellow]Attendee Not found. [/yellow]")
        
def delete_event():
    event_id = input("Enter Event ID to delete: ")
    event = Event.find_by_id(event_id)
    if event:
        event.delete()
        console.print(f"[red]Event {event.name} deleted.[/red]")
    else:
        console.print("[yellow]Event not found[/yellow]")

def find_by_event_name():
    name = input("Enter event name to search: ")
    events = Event.get_all()
    matching_events = [event for event in events if event.name == name]
    if matching_events:
        for event in matching_events:
            print(event)
    else:
        console.print("[yellow]No event found with that name.[/yellow]")

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

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
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
