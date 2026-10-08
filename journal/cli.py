import argparse
import sys
import questionary
from journal.core import add_entry, list_entries, search_entries
from rich.console import Console

console = Console()

def main_menu():
    """Displays an interactive main menu hub when no arguments are provided."""
    console.print("[bold cyan]📝 Markdown Personal Journal & Search CLI[/bold cyan]")
    
    action = questionary.select(
        "What would you like to do today?",
        choices=[
            "✨ Create a new entry",
            "📖 List all entries",
            "🔍 Search entries by keyword",
            "🚪 Exit"
        ]
    ).ask()

    if not action or "Exit" in action:
        console.print("[yellow]Goodbye![/yellow]")
        sys.exit(0)
    
    elif "Create" in action:
        handle_new_entry()
    elif "List" in action:
        handle_list_entries()
    elif "Search" in action:
        handle_search_entries()

def handle_new_entry(title=None, content=None, tags=None):
    if not title:
        title = questionary.text("Enter entry title:").ask()
        if not title:
            console.print("[red]Title cannot be empty![/red]")
            return

    if not content:
        content = questionary.text(
            "Enter entry content/body (Press Alt+Enter or Esc+Enter to submit multiline):", 
            multiline=True
        ).ask()
        if not content:
            console.print("[red]Content cannot be empty![/red]")
            return

    if not tags:
        tags = questionary.text("Enter optional tags (comma-separated):").ask()

    path = add_entry(title, content, tags or "")
    console.print(f"[bold green]✨ Success! Created entry at:[/bold green] {path}")

def handle_list_entries():
    files = list_entries()
    if not files:
        console.print("[yellow]No journal entries found yet. Create one![/yellow]")
    else:
        console.print("[bold cyan]📖 Your Journal Entries:[/bold cyan]")
        for f in files:
            console.print(f" - {f.name}")

def handle_search_entries(keyword=None):
    if not keyword:
        keyword = questionary.text("Enter keyword to search for:").ask()
        if not keyword:
            console.print("[red]Keyword cannot be empty![/red]")
            return

    results = search_entries(keyword)
    if not results:
        console.print(f"[yellow]No matches found for '{keyword}'.[/yellow]")
    else:
        console.print(f"[bold cyan]🔍 Found {len(results)} matching entries:[/bold cyan]")
        for r in results:
            console.print(f" - {r.name}")

def main():
    parser = argparse.ArgumentParser(description="Markdown Personal Journal & Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'new' command
    new_parser = subparsers.add_parser("new", help="Create a new journal entry")
    new_parser.add_argument("-t", "--title", help="Title of your entry")
    new_parser.add_argument("-c", "--content", help="Body text of your entry")
    new_parser.add_argument("--tags", default="", help="Optional tags separated by commas")

    # 'list' command
    subparsers.add_parser("list", help="List all journal entries")

    # 'search' command
    search_parser = subparsers.add_parser("search", help="Search entries by keyword")
    search_parser.add_argument("keyword", nargs="?", help="Keyword to search for")

    args = parser.parse_args()

    # If no command is provided, launch the interactive main menu hub!
    if not args.command:
        main_menu()
    elif args.command == "new":
        handle_new_entry(args.title, args.content, args.tags)
    elif args.command == "list":
        handle_list_entries()
    elif args.command == "search":
        handle_search_entries(args.keyword)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()