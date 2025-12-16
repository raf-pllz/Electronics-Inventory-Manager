# Creative Tools – Electronics Inventory Manager

A terminal-based Electronics Inventory Manager written in Python. The project provides a structured, mode-driven Command Line Interface (CLI) with colored output, contextual prompts, and JSON-based file management, designed to scale into a full inventory system.

---

## Overview

Creative Tools – Electronics Inventory Manager is a development-stage CLI application that allows users to interact with electronics inventory data through dedicated command modes. The system emphasizes clarity, modularity, and extensibility, while maintaining a clean terminal user experience.

The application currently supports JSON-based inventory files, stored in a dedicated database directory, and introduces contextual command prompts that adapt to the active mode.

---

## Features

- Interactive, mode-aware terminal interface
- ANSI-colored output and dynamic prompts
- Automatic database folder creation
- JSON-based inventory file handling
- Paged command navigation system
- Command-specific help inside command mode
- Clear separation between logic, data, and UI helpers

---

## Project Structure

```
.
├── main.py        # Main application in python
├── data.py        # Data used by main.py
├── README.md      # Project documentation
├── Database       # Software-Created folder for the .json files
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

* **Latest Version:** 1.2Dev
* **Release Date:** 16/12/2025

---

## Roadmap (Planned)

* Implement actual electronics inventory storage
* Persistent data storage (JSON)
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
