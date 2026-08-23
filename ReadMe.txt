

### `README.md`

Create a file named **`README.md`** in your project's root folder and paste the following content:

```markdown
# Flask Task Manager (PostgreSQL)

A full-stack Flask application integrated with a local PostgreSQL database, automated code formatting, and linting.

## Project Structure

```text
flask-task-app/
├── templates/          # HTML views
├── .env                # Database credentials (untracked)
├── .eslintrc.json      # ESLint rules for JS
├── .gitignore          # Files excluded from version control
├── .prettierignore     # Files excluded from Prettier formatting
├── .prettierrc         # Prettier formatting configuration
├── app.py              # Flask application & database models
├── cSpell.json         # Spell checker rules
├── package.json        # Project scripts & dev tool dependencies
└── README.md           # Documentation

```

## Setup Instructions

### 1. Environment Variables

Create a `.env` file in the root folder with the following variables:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=flask_tasks

```

### 2. Install Dependencies

**Python Virtual Environment:**

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows Git Bash
pip install flask flask-sqlalchemy psycopg2-binary python-dotenv black

```

**Node Tools (Prettier, ESLint, cSpell):**

```bash
npm install

```

## Available Scripts

* **Start Application:** Formats all project files and launches the Flask server:
```bash
npm start

```


* **Format Project:** Formats HTML/JS/JSON files via Prettier:
```bash
npm run format

```


* **Spell Check:** Scans project files for typos:
```bash
npm run spell-check

```



## Code Quality Tools

* **Black:** Automatic Python code formatting on save.
* **Prettier:** Formatting for HTML, JS, and JSON files.
* **cSpell & ESLint:** In-editor spell checking and JS error prevention.

```

```