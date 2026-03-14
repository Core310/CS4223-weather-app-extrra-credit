# Architecture

**Analysis Date:** 2025-05-22

## Pattern Overview

**Overall:** Multi-platform Weather Application suite.
- `2025f-feature-development-b`: Flask-based Web Application (Server-Side Rendering).
- `2025f-feature-development-c`: Tkinter-based Desktop Application (Event-driven GUI).

**Key Characteristics:**
- **External API Dependency:** Both applications rely on the OpenWeatherMap API for weather data.
- **Environment Driven:** Both utilize configuration or environment variables for API keys.
- **Visual Feedback:** Extensive use of static assets (icons, backgrounds) to represent weather states.

## Layers

**Presentation Layer (Web):**
- Purpose: Renders HTML templates with weather data.
- Location: `2025f-feature-development-b/templates/`
- Contains: Jinja2 templates (`index.html`, `city.html`, `error.html`).
- Depends on: `2025f-feature-development-b/main.py`
- Used by: End users via web browser.

**Presentation Layer (Desktop):**
- Purpose: Displays a GUI with weather information and icons.
- Location: `2025f-feature-development-c/app.py`
- Contains: Tkinter widgets and PIL-based image handling.
- Depends on: `2025f-feature-development-c/Icons/`, `2025f-feature-development-c/Images/`
- Used by: End users via local execution.

**Logic Layer (Web):**
- Purpose: Handles routing, API calls, and data transformation.
- Location: `2025f-feature-development-b/main.py`
- Contains: Flask routes, `requests` calls to OpenWeatherMap.
- Depends on: OpenWeatherMap API, `.env` for API keys.

**Logic Layer (Desktop):**
- Purpose: Manages GUI events, performs threaded API requests, and updates UI state.
- Location: `2025f-feature-development-c/app.py`
- Contains: `Weather` class, threading logic, `requests` calls.
- Depends on: OpenWeatherMap API, `config.ini` for API keys.

## Data Flow

**Weather Search (Web):**
1. User submits city via `POST` to `/` in `2025f-feature-development-b/main.py`.
2. App redirects to `/<city>`.
3. `get_weather(city)` calls Geocoding API to get coordinates.
4. App calls Current Weather and 5-day Forecast APIs using coordinates.
5. Data is passed to `city.html` and rendered for the user.

**Weather Search (Desktop):**
1. User enters city and clicks search or presses Enter.
2. `threading()` starts a new thread to run `__get_weather()`.
3. `__get_weather()` reads API key from `config.ini` and calls OpenWeatherMap API.
4. `__set_information()` processes the JSON response and updates Tkinter labels.
5. `place_image()` updates the weather icon based on the weather condition.

**State Management:**
- **Web:** Stateless at the server level; state is passed via URL parameters and rendered in templates.
- **Desktop:** Managed within the `Weather(Tk)` class instance via widget variables (e.g., `self.search_textbox`, `self.temperature`).

## Key Abstractions

**API Client (Web):**
- Purpose: Direct use of `requests` within route handlers.
- Examples: `2025f-feature-development-b/main.py`
- Pattern: Procedural API calls within controller functions.

**API Client (Desktop):**
- Purpose: Threaded API calls to keep GUI responsive.
- Examples: `2025f-feature-development-c/app.py` (method `__get_weather`).
- Pattern: Async-style background threading for I/O.

## Entry Points

**Flask Web App:**
- Location: `2025f-feature-development-b/main.py`
- Triggers: `python main.py` or WSGI server (see `Procfile`).
- Responsibilities: Server initialization, routing, template rendering.

**Tkinter Desktop App:**
- Location: `2025f-feature-development-c/app.py`
- Triggers: `python app.py`
- Responsibilities: GUI main loop, event handling.

## Error Handling

**Strategy:** Conditional redirection and message boxes.

**Patterns:**
- **Web:** Redirects to `/error` when city geocoding fails in `2025f-feature-development-b/main.py`.
- **Desktop:** Uses `tkinter.messagebox` to show warnings/errors for connection or API failures in `2025f-feature-development-c/app.py`.

## Cross-Cutting Concerns

**Logging:** Not explicitly implemented; uses standard output/exceptions.
**Validation:** Basic city name validation via API response checks.
**Authentication:** API Key management via `.env` (Web) or `config.ini` (Desktop).

---

*Architecture analysis: 2025-05-22*
