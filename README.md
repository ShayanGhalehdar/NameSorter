# Name Sorter

A clean, object-oriented CLI tool built in Python that reads a list of full names from a text file, validates each entry against domain constraints, and sorts them primarily by surname and secondarily by given names.

---

## Domain Rules & Constraints

According to the specification:
- A name must have **at least 1 given name** and **up to 3 given names**.
- Combined with **1 last name**, a valid name contains between **2 and 4 parts** (e.g., `Marin Alvarez` to `Hunter Uriah Mathew Clarke`).
- Names with fewer than 2 tokens (e.g., `Madonna`) or more than 4 tokens (e.g., `A B C D E`) are rejected with a descriptive validation error.
- Sorting order:
  1. Primary key: **Last name** (alphabetical).
  2. Secondary key (tie-breaker): **Given names** in left-to-right order.

---

## Project Structure

```text
name-sorter/
├── README.md
├── name_sorter.py
└── tests/
    ├── __init__.py
    ├── test_name.py
    ├── test_name_sorter.py
    └── test_cli.py
```

---

## Requirements

- Python 3.10+
- `pytest` (for running the automated test suite)

---

## Setup & Installation

### 1. Install Dependencies
```bash
python3 -m pip install pytest
```

### 2. Make the Script Executable
```bash
chmod +x name_sorter.py
```

### 3. Expose the `name-sorter` Command
To run the application with the exact assessment command (`name-sorter ./unsorted-names-list.txt`), create a symlink in a directory that is on your `$PATH` (such as `~/.local/bin`):

```bash
mkdir -p ~/.local/bin
ln -sf "$(pwd)/name_sorter.py" ~/.local/bin/name-sorter
```

---

## Running the Application

### Using the Installed Command
```bash
name-sorter ./unsorted-names-list.txt
```

### Running Directly via Python
```bash
python3 name_sorter.py ./unsorted-names-list.txt
```

### Output Behavior
1. Prints the sorted names directly to standard output (`stdout`).
2. Overwrites or creates `sorted-names-list.txt` in the current working directory with the formatted output.

---

## Running the Tests

Run the full test suite using the same Python interpreter:

```bash
python3 -m pytest -v
```

To run a specific test file:
```bash
python3 -m pytest tests/test_name.py -v         # Domain model & validation tests
python3 -m pytest tests/test_name_sorter.py -v  # Core sorting & tie-breaking tests
python3 -m pytest tests/test_cli.py -v          # CLI integration tests
```
