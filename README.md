# Markdown Personal Journal & Search CLI (`markdown-journal-cli`)

A lightweight, 100% offline, privacy-first command-line journal tool built with Python. Write, store, list, and search through your markdown notes effortlessly without needing any external API keys or cloud databases.

---

## ✨ Features

- **Markdown Storage:** All entries are saved as clean, portable `.md` files.
- **Interactive Prompts:** Guided terminal menus using `questionary` with multi-line writing support.
- **Custom Directory Support:** Point your journal to any folder on your computer (like an Obsidian vault or custom directory) using the `JOURNAL_DIR` environment variable.
- **Robust Fallback:** Automatically defaults to a safe local directory if custom paths fail.
- **Fast Search & Listing:** Easily search your entire journal history by keyword.

---

## 🚀 Installation

1. Clone or download this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/markdown-journal-cli.git](https://github.com/YOUR_USERNAME/markdown-journal-cli.git)
   cd markdown-journal-cli

Install the required dependencies:

Bash
pip install -r requirements.txt
📖 Usage
1. Create a New Entry
Run the command interactively:

Bash
python -m journal.cli new
(Or provide flags directly: python -m journal.cli new -t "My Title" -c "My Content")

2. List All Entries
Bash
python -m journal.cli list
3. Search Entries
Bash
python -m journal.cli search "keyword"
📂 Custom Storage Location
By default, notes are saved in your user profile (~/.markdown_journal). You can change this to any folder by setting the JOURNAL_DIR environment variable:

PowerShell:

PowerShell
$env:JOURNAL_DIR="C:\Users\YourUsername\Documents\MyJournal"
python -m journal.cli new
🛠️ Tech Stack
Python (Core logic & CLI arguments)

Rich (Stunning terminal styling and feedback)

Questionary (Interactive prompts and multi-line editor)

Markdown (Markdown support)