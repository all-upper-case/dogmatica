# Dogmatica

Welcome to the **Dogmatica** repository. This project serves as a small tutorial-style example of how a typical Python project might be laid out on GitHub.

## Repository layout

- `src/` – the source code for the `dogmatica` package.
- `tests/` – unit tests for the code in `src/`.
- `docs/` – extra documentation and guides.
- `.gitignore` – patterns for files Git should ignore.
- `requirements.txt` – Python dependencies used for development.
- `LICENSE` – the open‑source license for this project (MIT).

## Getting started

1. Ensure you have Python 3.8 or newer installed.
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies and the package in editable mode:

   ```bash
   pip install -e . -r requirements.txt
   ```
4. Run the tests to make sure everything works:

   ```bash
   pytest
   ```

## Next steps

Browse the files under `src/`, `tests/`, and `docs/` to see how a simple project is structured. Feel free to experiment—add new modules, write additional tests, or expand the documentation.

