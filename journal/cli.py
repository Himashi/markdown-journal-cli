import argparse
import sys
import questionary
from journal.core import add_entry, list_entries, search_entries
from rich.console import Console

console = Console()

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
    search_parser.add_argument("keyword", help="Keyword to search for")

    args = parser.parse_args()

    if args.command == "new":
        # Interactive prompts if title or content are missing
        title = args.title
        if not title:
            title = questionary.text("Enter entry title:").ask()
            if not title:
                console.print("[red]Title cannot be empty![/red]")
                sys.exit(1)

        content = args.content
        if not content:
            content = questionary.text(
                "Enter entry content/body (Press Alt+Enter or Esc+Enter to submit multiline):", 
                multiline=True
            ).ask()
            if not content:
                console.print("[red]Content cannot be empty![/red]")
                sys.exit(1)

        tags = args.tags
        if not tags:
            tags = questionary.text("Enter optional tags (comma-separated):").ask()

        path = add_entry(title, content, tags or "")
        console.print(f"[bold green]✨ Success! Created entry at:[/bold green] {path}")

    elif args.command == "list":
        files = list_entries()
        if not files:
            console.print("[yellow]No journal entries found yet. Use 'new' to create one![/yellow]")
        else:
            console.print("[bold cyan]📖 Your Journal Entries:[/bold cyan]")
            for f in files:
                console.print(f" - {f.name}")

    elif args.command == "search":
        results = search_entries(args.keyword)
        if not results:
            console.print(f"[yellow]No matches found for '{args.keyword}'.[/yellow]")
        else:
            console.print(f"[bold cyan]🔍 Found {len(results)} matching entries:[/bold cyan]")
            for r in results:
                console.print(f" - {r.name}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()