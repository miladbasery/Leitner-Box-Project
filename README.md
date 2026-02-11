# 🧠 Leitner Box Project

### High-Performance Spaced Repetition System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-336791?style=for-the-badge&logo=postgresql)

**Leitner Box Project** is a robust, terminal-based implementation of the Leitner System, designed for efficient memory retention through algorithmic spaced repetition. Built with Python and PostgreSQL, it features persistent storage, user authentication, and an automated penalty system for overdue cards.

---

## 📑 Table of Contents

- [Architecture & Features](#-architecture--features)
- [Algorithmic Logic](#-algorithmic-logic)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)

---

## 🏗 Architecture & Features

The application is structured as a modular CLI tool interacting with a relational database backend.

* **Persistent Storage:** Utilizes `psycopg2` for robust interaction with a PostgreSQL database.
* **User Authentication:** Secure registration and login flows with regex-based input validation.
* **Automated Schema Management:** Self-healing database setup; automatically detects and initializes the database and tables (`users`, `cards`) upon first launch.
* **Multi-Slot Leitner System:** Supports a 6-slot learning pipeline.
* **Graceful Error Handling:** Comprehensive `try-except` blocks for database transactions and user I/O.

---

## 🧮 Algorithmic Logic

### 1. Spaced Repetition Review
The core review mechanism retrieves cards from specific slots based on user selection.
* **Success (`y`):** The card is promoted to `Current Slot + 1`.
* **Failure (`n`):** The card remains in the `Current Slot` (Retention Strategy).

### 2. The Penalty Policy
To ensure consistency, the system runs a background check (`apply_penalty_policy`) before every review session:
* **Calculation:** `Deadline = Last Review Date + Slot Interval + 2 Days (Grace Period)`
* **Penalty:** If the current date exceeds the `Deadline`, the card is demoted:
    $$New Slot = \max(1, Current Slot - 1)$$

---

## ⚡ Installation

### Prerequisites
* Python 3.8+
* PostgreSQL Server installed and running

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/miladbasery/Leitner-Box-Project.git
    cd Leitner-Box-Project
    ```

2.  **Set up Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install psycopg2-binary
    ```

---

## ⚙️ Configuration

The application requires a `config.py` file in the root directory to handle database credentials and Leitner intervals.

1.  Create a file named `config.py` in the root folder.
2.  Paste the following configuration (adjust credentials as needed):

```python
# config.py

# Database Credentials
DB_NAME = "leitner_db"
DB_USER = "postgres"
DB_PASS = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

# Leitner System Intervals (Slot: Days)
# Defines how often cards in each slot should be reviewed
BOX_INTERVALS = {
    1: 1,   # Review every day
    2: 2,   # Review every 2 days
    3: 4,   # Review every 4 days
    4: 8,   # Review every 8 days
    5: 16,  # Review every 16 days
    6: 30   # Review every month
}
```
### Member pf team
**Mr . Milad basery**

