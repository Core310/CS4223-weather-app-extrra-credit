# Codebase Structure

**Analysis Date:** 2025-05-22

## Directory Layout

```
[project-root]/
├── 2025f-feature-development-b/     # Flask Web Application
│   ├── static/                       # Static CSS and assets
│   │   ├── assets/                   # Weather condition images/backgrounds
│   │   └── css/                      # Application styling
│   ├── templates/                    # Jinja2 HTML templates
│   ├── main.py                       # Main application logic and routing
│   ├── requirements.txt              # Dependencies (Flask, requests, etc.)
│   └── Procfile                      # Deployment configuration
└── 2025f-feature-development-c/     # Tkinter Desktop Application
    ├── Icons/                        # Weather condition icons
    ├── Images/                       # UI interface graphics (buttons, etc.)
    ├── app.py                        # Main GUI application logic
    └── config.ini                    # API configuration
```

## Directory Purposes

**2025f-feature-development-b/static:**
- Purpose: Serves static files to the client.
- Contains: Images and CSS.
- Key files: `static/css/main.css`.

**2025f-feature-development-b/templates:**
- Purpose: HTML structure for the web app.
- Contains: `index.html` (Home), `city.html` (Weather Details), `error.html` (Error Page).

**2025f-feature-development-c/Icons:**
- Purpose: Weather state visualization for the desktop app.
- Contains: Weather-specific PNG files (`clear.png`, `rain.png`, etc.).

**2025f-feature-development-c/Images:**
- Purpose: UI components for the Tkinter interface.
- Contains: Logos, buttons, and decorative borders.

## Key File Locations

**Entry Points:**
- `2025f-feature-development-b/main.py`: Main entry for the web app.
- `2025f-feature-development-c/app.py`: Main entry for the desktop app.

**Configuration:**
- `2025f-feature-development-b/.env` (implicitly used): For `OWM_API_KEY`.
- `2025f-feature-development-c/config.ini`: Stores the OpenWeatherMap API key.

**Core Logic:**
- `2025f-feature-development-b/main.py`: Handles Flask routing and weather data processing.
- `2025f-feature-development-c/app.py`: Handles Tkinter GUI state and API requests.

## Naming Conventions

**Files:**
- Snake Case: `main.py`, `app.py`.
- Lowercase with hyphens for assets: `weather-home-background.jpg`.

**Directories:**
- Categorical: `static`, `templates`, `Icons`, `Images`.

## Where to Add New Code

**New Web Feature:**
- Logic: `2025f-feature-development-b/main.py`
- UI: `2025f-feature-development-b/templates/*.html`
- Styles: `2025f-feature-development-b/static/css/main.css`

**New Desktop Feature:**
- Implementation: `2025f-feature-development-c/app.py`
- New Assets: `2025f-feature-development-c/Icons/` or `2025f-feature-development-c/Images/`

**Shared Logic (Future):**
- Create a shared module in the root directory to deduplicate OpenWeatherMap API call logic.

## Special Directories

**2025f-feature-development-b/python-weather-app:**
- Purpose: Possibly a sub-repository or redundant folder.
- Committed: Yes.

**2025f-feature-development-b/screenshots:**
- Purpose: Visual documentation of the web application.
- Committed: Yes.

---

*Structure analysis: 2025-05-22*
