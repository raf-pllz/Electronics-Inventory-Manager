# Creative Tools – Electronics Inventory Manager

A lightweight, terminal-based Electronics Inventory Manager written in Python. The project focuses on providing a simple command-line interface (CLI) with colored output, basic command handling, and an extensible structure suitable for further development.

---

## Overview

Creative Tools – Electronics Inventory Manager is an early-stage (development version) CLI application designed to manage and present information through a command-driven terminal environment. It demonstrates:

* ANSI color usage for improved terminal UX
* Modular command handling
* A simple interactive command loop
* Clear separation between UI, logic, and commands

This repository currently represents a **development preview** and serves as a foundation for future inventory-related features.

---

## Features

* Interactive terminal interface
* Colored command prompt and output
* Built-in commands:

  * `/help`
  * `/about`
  * `/commands`
  * `/quit`

* Basic error handling for unknown commands
* Structured and readable Python codebase

---

## Project Structure

```
.
├── main.py        # Main application in python
├── data.py        # Data used by main.py
├── README.md      # Project documentation
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

### Available Commands

* `/help`
  Displays the most important and frequently used commands.

* `/about`
  Shows software information such as version, release date, and author details.

* `/commands`
  Displays the full list of available commands.

* `/quit`
  Exits the application.
  
---

## Version Information

* **Version:** 1.0Dev
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

This project is currently shared for illustration and archiving purposes. Licensing terms may be defined in a future release, but until then, you are not allowed to use any part of this code/sofware.
