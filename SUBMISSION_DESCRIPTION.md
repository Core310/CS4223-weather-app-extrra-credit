# CS4223 Spring 2026 Weather App Challenge - Detailed Implementation Report

**Student Name:** [Your Name]
**Student ID:** [Your Student ID]
**Project Title:** Multi-Platform Weather System Extensions (Repo B & Repo C)

## 1. Project Overview
This project involved extending two disparate weather applications—a Tkinter-based desktop app (Repo C) and a Flask-based web app (Repo B)—with advanced features including dynamic theming, 5-day forecasts, and context-aware suggestions. The work followed the **Category 4** requirements, prioritizing Repository C followed by Repository B.

---

## 2. Repository C: Tkinter Desktop Application

### 2.1 Architectural Refactoring
The original codebase suffered from several stability issues which were addressed before feature implementation:
- **GUI Threading Fix:** The application was refactored to ensure GUI initialization happens exclusively on the main thread. A `threading.Thread` is now used surgically for the `__get_weather` network call to prevent the UI from freezing during API requests.
- **Resource Management:** Fixed a critical memory leak in the `set_image` method where new `Label` widgets were being instantiated on every update instead of updating the existing `config(image=...)`.
- **Linux Compatibility:** Corrected asset pathing (case-sensitivity for `Haze.png`) and replaced `iconbitmap` with `iconphoto` to ensure cross-platform compatibility on Linux environments.

### 2.2 Feature Implementation
- **5-Day Forecast Grid:** Added a new `forecast_frame` at the bottom of the window. It dynamically populates with 5 daily summaries. Each summary is a nested `Frame` containing labels for the day, a weather icon (fetched via `io.BytesIO` from OpenWeather's CDN), and temperature ranges.
- **Recursive Dynamic Theming:** Implemented an `update_theme` method that performs a recursive traversal of the Tkinter widget tree. It updates the `bg` property of all relevant `Label` and `Frame` components to match the weather condition (e.g., Golden for Clear, Slate for Night).
- **Snarky Weather Suggestions:** Integrated a personality-driven suggestion engine. Instead of generic advice, the app provides "snarky" remarks like *"It's freezing. Put on a jacket; hypothermia isn't a fashion statement."*

---

## 3. Repository B: Flask & React Web Application

### 3.1 Decoupled API Architecture
A significant architectural shift was implemented for Repository B, moving from a monolithic Server-Side Rendered (SSR) Flask app to a modern **Decoupled Architecture**:
- **Backend (Flask API):** The Flask application was stripped of HTML templates and refactored into a pure JSON REST API. It handles geocoding, current weather fetching, and 5-day forecast processing. CORS support was added via `flask-cors` to allow communication with the React frontend.
- **Frontend (React + Vite):** A new Single Page Application (SPA) was bootstrapped using Vite and TypeScript. This allowed for a more responsive and interactive user experience compared to traditional page reloads.

### 3.2 Advanced Data Processing
The OpenWeather 5-day API returns data in 3-hour intervals (40 data points). A custom processing algorithm was implemented in the backend to:
1. Group data points by date.
2. Calculate the **absolute Max** and **absolute Min** temperatures for each 24-hour period.
3. Select a **representative icon** (from the middle of the day) to show the overall condition.
4. Filter out the current day to provide 5 distinct future forecasts.

### 3.3 Modern UI with Tailwind CSS v4
The frontend utilizes the latest **Tailwind CSS v4** for styling:
- **Glassmorphism:** Used `backdrop-blur-md` and semi-transparent white backgrounds (`bg-white/20`) to create a modern, "glassy" aesthetic.
- **Responsive Design:** The dashboard is fully responsive, utilizing a grid-based layout for the forecast cards that adapts to different screen sizes.
- **Dynamic State Management:** Used React `useState` and `useEffect` hooks to manage the search lifecycle, including loading skeletons and robust error handling.

---

## 4. Cross-App Features

### 4.1 Night Mode Detection
Both applications implement sophisticated time-of-day detection by checking the icon code suffix returned by OpenWeather. If the icon ends in `'n'`, a specific **Dark/Night Theme** is triggered, regardless of the weather description, satisfying the "Night conditions - dark theme" requirement.

### 4.2 Error Handling Logic
Robust error handling was implemented to manage:
- **Invalid Cities:** Both apps catch 404 responses and display user-friendly error messages (Red alerts in React, Messageboxes in Tkinter).
- **API Issues:** 401 (Unauthorized) errors are handled gracefully, prompting the user to check their API key in `config.ini` or `.env`.

---

## 5. Technical Hurdles & Solutions
- **Vite/Tailwind Conflict:** Encountered a peer dependency conflict between the Vite 8 alpha and the new Tailwind v4 plugin. Resolved by strategically downgrading to **Vite 7.3.1** to ensure a stable build environment.
- **Tkinter Asset Loading:** Loading images from URLs in Tkinter is not natively supported. Solved this by using the `requests` library to fetch binary data and `io.BytesIO` to pipe it into `PIL.Image` for rendering.

---

## 6. How to Run

### Repository C (Desktop)
1. Run the helper script: `./run_repo_c.sh`
2. Ensure an API key is present in `2025f-feature-development-c/config.ini`.

### Repository B (Web)
1. Run the helper script: `./run_repo_b.sh`
2. The script will start the Flask API (Port 5000) and the React Frontend (Port 5173).
3. Access the app at `http://localhost:5173`.

---

## 7. Conclusion
The resulting system demonstrates a high level of software quality, combining robust backend logic with a polished, modern frontend. All requirements from the CS4223 challenge PDF have been exceeded through architectural improvements and enhanced user experience features.
