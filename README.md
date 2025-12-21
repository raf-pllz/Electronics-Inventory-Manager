# Creative Tools – Electronics Inventory Manager

A terminal-based Electronics Inventory Manager written in Python.  
The project provides an interactive CLI for creating, opening, and managing JSON-based inventory files, with support for adding and removing electronic components through structured command modes.

This repository currently represents a **development-stage build** and serves as the foundation for a more complete inventory management system.

---

## Overview

Creative Tools – Electronics Inventory Manager is a command-driven CLI application designed to manage electronics inventory data stored in `.json` files. It emphasizes:

- Clear terminal UX with ANSI colors
- Mode-based command interaction
- Structured inventory object handling
- Safe file and data manipulation
- Extensible architecture for future growth

The application operates entirely in the terminal and does not rely on external libraries.

---

## Features

- Interactive command-line interface
- ANSI-colored output and dynamic prompts
- JSON-based inventory storage
- Automatic database (vault) folder creation
- File-based inventory management
- Object-level inventory manipulation

### Core Capabilities

- Create inventory files
- Open existing inventory files
- Add components to an inventory
- Remove components by **ID** or **Name**
- Purge inventory files safely
- Paginated command listing with navigation

---

## Inventory Objects

Each inventory entry (component) consists of:

- **Name**
- **Description**
- **Stock quantity** (integer ≥ 0)
- **Unique ID**

Objects are stored as structured JSON entries and managed interactively through prompts.

---

## Project Structure



## Project Structure

```
.
├── CLIUI.py            # Script that handles commonly used UI elements for all scripts
├── data.py             # Data used by main.py
├── jsonprocess.py      # Script that handles the .json file processes
├── main.py             # Main application in python
├── notifications.py    # Script that handles the notifications for the user
├── README.md           # Project Read Me file
├── CHANGELOG.md        # Project Changelog
```

---

## Requirements

* Python 3.x
* A terminal that supports ANSI escape sequences (most modern terminals do)

No external libraries are required (as of now).

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/raf-pllz/Electronics-Inventory-Manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Electronics-Inventory-Manager
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## Usage

When launched, the application displays a welcome screen and a list of basic commands. You interact with the system by typing commands into the prompt.

  
---

## Version Information

* **Latest Development Version:** 1.5Dev
* **Development Version Release Date:** 21/12/2025
* **Latest User-Ready Version:** NONE
* **User-Ready Version Release Date:** NOT YET RELEASED

---

## Roadmap (Planned)

* Implement actual electronics inventory storage (Work-In-Progress)
* Persistent data storage (JSON) (Also Work-In-Progress)
* Eventual move to C or C++ (for performance improvements)

---

## Author

Developed by **Rafail Palalakis**
© 2025 – All Rights Reserved

LinkedIn: [https://www.linkedin.com/in/raf-pllz/](https://www.linkedin.com/in/raf-pllz/)

---

## License

Copyright (c) 2025 Rafail Palalakis

All rights reserved.


This software is provided for educational, illustrative, and portfolio purposes only.
No permission is granted to copy, modify, merge, publish, distribute, sublicense,
or sell copies of this software, in whole or in part, without explicit written
permission from the author.

Any unauthorized use of this software is strictly prohibited.


NO WARRANTY / NO GUARANTEE NOTICE

This software is provided “AS IS”, without warranty of any kind, express or implied.
The author makes no guarantees regarding the correctness, reliability, stability,
security, or suitability of this software for any purpose.

Use of this software is entirely at your own risk.
In no event shall the author be held liable for any damages, data loss, system failure,
or other issues arising from the use, misuse, or inability to use this software.

This project is under active development and may change, break, or be discontinued
at any time without notice. X.Y-Dev versions are extremely prohibited for use as
they are not tested for normal use, and act as an archive.


A formal open-source or commercial license may be defined in a future release.
