# Changelog

All notable changes to **Creative Tools – Electronics Inventory Manager** are documented in this file.

The project is currently in active development and uses a development-based versioning scheme (`X.Y-Dev`).

---

## [1.5Dev] – 21/12/2025

### Added
- Component management inside opened inventory files:
  - `/add` command for creating new inventory objects.
  - `/remove` command with sub-modes for deletion by **ID** or **Name**.
- Structured component model including:
  - Object Name
  - Description
  - Stock (validated integer ≥ 0)
  - Object ID
- JSON write and delete operations through centralized processing utilities.
- Confirmation step for destructive operations (file purge and object removal).
- Success notifications for object creation and deletion.
- File-level operational mode with context-aware prompts.

### Improved
- Input validation for numeric fields (stock values).
- Error feedback when invalid object identifiers are provided.
- State restoration when exiting nested modes (`/exit` handling consistency).
- Clearer separation between command display mode, file mode, and creation/purge workflows.
- CLI UX consistency through reusable UI helpers.

### Fixed
- Edge cases where invalid input could break command flow.
- Multiple instances of duplicated setter calls and silent failures.
- Incorrect handling of non-`.json` files during open and purge operations.

### Notes
- As of this version, the `/add` and `/remove` commands **do not perform duplicate checks** on existing objects.
- Objects with identical names or IDs may be created if the user provides them.
- This behavior is **known and intentional for the current development stage** and is planned to be improved in future versions with stricter validation and conflict handling.


## [1.4Dev] – 18/12/2025 (1st commit of the Day)

### Added
- Added contextual command access inside `/open`, `/create`, and `/purge` modes (e.g. `/commands` available while inside modes).
- Expanded `/about` output to include GitHub repository link.

### Improved
- Improved command list pagination logic and navigation (`/next`, `/prev`, `/exit`) with clearer UI output.
- Improved file handling robustness with explicit permission and existence checks.
- Standardized success, warning, and error messages for better terminal readability.


### Fixed
- Prevented invalid file types from being opened or purged.
- Fixed edge cases where missing folders or permission errors could cause silent failures.
- Improved exit handling across nested command modes to ensure clean state restoration.

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
