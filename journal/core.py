import pathlib
import markdown

# Define your journal storage directory (e.g., in user home or current folder)
JOURNAL_DIR = pathlib.Path.home() / ".markdown_journal"

def init_journal():
    """Ensures the journal directory exists."""
    JOURNAL_DIR.mkdir(parents=True, exist_ok=True)

def add_entry(title, content, tags=""):
    """Creates a new markdown journal entry file."""
    init_journal()
    # Format filename safely from title
    safe_title = "".join(c if c.isalnum() else "_" for c in title).lower()
    file_path = JOURNAL_DIR / f"{safe_title}.md"
    
    file_content = f"# {title}\n\n**Tags:** {tags}\n\n{content}\n"
    file_path.write_text(file_content, encoding="utf-8")
    return file_path

def list_entries():
    """Returns a list of all journal markdown files."""
    init_journal()
    return list(JOURNAL_DIR.glob("*.md"))

def search_entries(keyword):
    """Searches for keyword inside journal files."""
    init_journal()
    matches = []
    for file_path in JOURNAL_DIR.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        if keyword.lower() in content.lower():
            matches.append(file_path)
    return matches

def export_entries_to_html(output_dir="export"):
    """Converts all markdown journal entries into clean, styled HTML files."""
    out_path = pathlib.Path(output_dir)
    out_path.mkdir(exist_ok=True)
    
    files = list_entries()
    exported_files = []
    
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            max-width: 700px;
            margin: 40px auto;
            padding: 0 20px;
            line-height: 1.6;
            color: #24292e;
            background-color: #f6f8fa;
        }}
        .container {{
            background: #ffffff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}
        h1 {{ border-bottom: 2px solid #eaecef; padding-bottom: 10px; margin-top: 0; }}
        pre {{ background: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }}
        code {{ font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace; }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

    for file_path in files:
        markdown_content = file_path.read_text(encoding="utf-8")
        html_body = markdown.markdown(markdown_content, extensions=['fenced_code', 'tables'])
        
        title = file_path.stem
        final_html = html_template.format(title=title, content=html_body)
        
        dest_file = out_path / f"{file_path.stem}.html"
        dest_file.write_text(final_html, encoding="utf-8")
        exported_files.append(dest_file)
        
    return exported_files