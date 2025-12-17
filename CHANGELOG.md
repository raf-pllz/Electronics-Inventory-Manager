# Changelog

All notable changes to **Creative Tools – Electronics Inventory Manager** are documented in this file.

The project is currently in active development and uses a development-based versioning scheme (`X.Y-Dev`).

---

## [1.3Dev] – 17/12/2025 (1st Commit of the Day)

### Added

* `/purge` command with dedicated **Purge/Delete Mode**.

### Improved

* Error and mode handling by all the modes present (since some weird behaviour was found)

### Fixed

* Further Prompt inconsistencies across command modes.

---

## [1.2Dev] – 16/12/2025 (3rd Commit of the Day)

### Added

* JSON-based inventory file system using a dedicated `Database/` directory.
* `/open` command with dedicated **Open Mode**.
* `/create` command with dedicated **Create Mode**.
* Dynamic command prompt that reflects the active mode (default, commands, open, create, file).
* ASCII Art logo display in `/about` command.

### Improved

* Refactored architecture with shared configuration and utilities in `data.py`.
* Centralized access prompt generation via `ACCTEXT`.
* Safer file handling with extension validation (`.json` only).
* Automatic database folder creation on startup (if there isn't one present).

### Fixed

* Prompt inconsistencies across command modes.
* File name handling when opening or creating JSON files.

---

## [1.1Dev] – 16/12/2025 (2nd Commit of the Day)

### Added

* Paginated command list system for `/commands`.
* Commands Mode with navigation support.
* Navigation commands: `/next`, `/prev`, `/exit`.

### Improved

* Command prompt context awareness.
* UI consistency across pages and modes.

### Fixed

* Duplicate command entries.
* Formatting inconsistencies in command output.

---

## [1.0Dev] – 16/12/2025

### Initial Release

### Added

* Core CLI framework.
* ANSI color support.
* Basic command loop and error handling.
* Initial command set: `/help`, `/about`, `/commands`, `/quit`.

---

© 2025 Rafail Palalakis. All rights reserved.
