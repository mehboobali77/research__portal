# Research Opportunities

A small web app for browsing, searching, adding, editing and deleting university research opportunities. Built with **Flask**, **Flask-SQLAlchemy** and **SQLite**, with a single-page HTML/JavaScript front end.

## Features

- View all research opportunities as cards (title, faculty, department, description, skills, positions, deadline, status)
- Search by title, area, faculty, department or skill
- Filter by status (Open / Closed)
- Add, edit and delete opportunities through a pop-up form
- Server-side validation with clear error messages
- Data is stored in a local SQLite database (created automatically)

## Tech Stack

| Layer    | Technology                    |
|----------|-------------------------------|
| Backend  | Python 3, Flask               |
| Database | SQLite via Flask-SQLAlchemy   |
| Frontend | HTML, CSS, vanilla JavaScript |

## Project Structure

```
research-opportunities/
├── app.py              # Flask app, database model and REST API
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── templates/
    └── index.html      # Front-end page (must be inside "templates")
```

The SQLite database file (`opportunities.db`) is created automatically in an `instance/` folder the first time you run the app.

## Requirements

- Python 3.9 or newer
- pip
- VS Code (recommended) with the Python extension

## Setup and Run

1. Open the project folder in a terminal (or VS Code's integrated terminal).

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it:

   - Windows (PowerShell): `venv\Scripts\Activate.ps1`
   - Windows (Command Prompt): `venv\Scripts\activate.bat`
   - macOS / Linux: `source venv/bin/activate`

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   python app.py
   ```

6. Open your browser at **http://127.0.0.1:5000**

Press `Ctrl + C` in the terminal to stop the server.

## API Endpoints

| Method | Endpoint                     | Description                  |
|--------|------------------------------|------------------------------|
| GET    | `/`                          | Web page                     |
| GET    | `/api/researchtitles`        | List all opportunities       |
| GET    | `/api/researchtitles/<id>`   | Get one opportunity          |
| POST   | `/api/researchtitles`        | Create an opportunity        |
| PUT    | `/api/researchtitles/<id>`   | Update an opportunity        |
| DELETE | `/api/researchtitles/<id>`   | Delete an opportunity        |

### Example request body (POST / PUT)

```json
{
  "title": "Machine Learning for Crop Disease Detection",
  "description": "Build image models to detect diseases in wheat leaves.",
  "area": "Artificial Intelligence",
  "faculty": "Dr. Ayesha Khan",
  "department": "Computer Science",
  "skills": "Python, TensorFlow, Data Analysis",
  "positions": 2,
  "deadline": "2026-12-31",
  "status": "Open"
}
```

All fields are required. `positions` must be a whole number that is 0 or greater.

## Troubleshooting

- **`TemplateNotFound: index.html`**: move `index.html` into a folder named `templates` next to `app.py`.
- **`ModuleNotFoundError: No module named 'flask'`**: activate the virtual environment and run `pip install -r requirements.txt`.
- **PowerShell blocks activation**: run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again.
- **Port 5000 already in use**: change the last line of `app.py` to `app.run(debug=True, port=5001)`.
- **Reset the data**: stop the app and delete the `instance/opportunities.db` file.
# research__portal
