# Changelog

All notable changes to **Creative Tools – Electronics Inventory Manager** are documented in this file.

The project follows a simple development-based versioning scheme (`X.YDev`) while the software is in active development.

---

## [1.1Dev] – 16/12/2025 (2nd Commit of the Day)

### Added

* Paged command list system for `/commands`.
* New sub-command mode for command browsing with its own prompt context.
* Navigation commands:

  * `/next` – Move to the next page of commands.
  * `/prev` – Move to the previous page of commands.
  * `/exit` – Exit command display mode.
* Dynamic page calculation for command lists.

### Improved

* Command prompt now reflects the current context (normal mode vs command display mode).
* Overall CLI structure refactored for better readability and scalability.
* Consistent UI separators using dynamic line length.

### Fixed

* Duplicate command entries in help output.
* Inconsistent command formatting across different views.

---

## [1.0Dev] – 16/12/2025

### Initial Release

### Added

* Core CLI framework.
* ANSI color support for improved terminal UX.
* Basic command handling loop.
* Initial commands:

  * `/help`
  * `/about`
  * `/commands` (basic placeholder)
  * `/quit`
* Error handling for unknown commands.

### Notes

* This version serves as the foundational architecture for future inventory-related features.
* No persistent data storage implemented at this stage.


---

© 2025 Rafail Palalakis. All rights reserved.
