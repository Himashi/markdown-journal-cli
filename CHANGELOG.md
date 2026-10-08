# Changelog

All notable changes to this project will be documented in this file.

## 1.0.0
- Initial stable release of Markdown Personal Journal & Search CLI (`markdown-journal-cli`).
- Core CLI commands: `new`, `list`, and `search` for local markdown journal entries.
- Custom storage directory support via the `JOURNAL_DIR` environment variable with robust path expansion and a safe fallback mechanism to the user's home folder.
- Interactive prompting menus using `questionary` when command-line arguments are omitted.
- Multi-line body writing support (using Alt+Enter) for long, detailed journal entries.
- Stunning terminal formatting, tables/lists, and color-coded feedback messages using `rich`.