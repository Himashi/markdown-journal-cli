import os
import datetime
from pathlib import Path

def get_journal_dir() -> Path:
    """Gets the active journal directory from environment variables or defaults to home safely."""
    env_dir = os.getenv("JOURNAL_DIR")
    if env_dir:
        path = Path(env_dir).expanduser()
    else:
        path = Path.home() / ".markdown_journal"
    
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception:
        # Fallback to home directory if custom path fails due to permissions or sync issues
        path = Path.home() / ".markdown_journal"
        path.mkdir(parents=True, exist_ok=True)
        
    return path

def add_entry(title: str, content: str, tags: str = ""):
    journal_dir = get_journal_dir()
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"{today}-{title.lower().replace(' ', '-')}.md"
    filepath = journal_dir / filename
    
    formatted_content = f"# {title}\n\n**Date:** {today}\n**Tags:** {tags}\n\n---\n\n{content}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(formatted_content)
    return filepath

def list_entries():
    journal_dir = get_journal_dir()
    files = sorted(journal_dir.glob("*.md"), reverse=True)
    return files

def search_entries(keyword: str):
    journal_dir = get_journal_dir()
    matching_files = []
    for filepath in journal_dir.glob("*.md"):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            if keyword.lower() in text.lower():
                matching_files.append(filepath)
    return matching_files