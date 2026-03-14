# Roadmap: CS4223 Spring 2026 Weather App Challenge

## Overview
This roadmap outlines the phased implementation of features for both the Tkinter Desktop App (Repo C) and the Flask Web App (Repo B).

## Phase 1: Repository C - Base Feature Implementation (Tkinter)
**Goal:** Implement dynamic background themes and weather-based suggestions for the desktop app.
**Requirements:** [FR1.2, FR3.1]
**Plans:** 1 plan

Plans:
- [ ] phase_1/PLAN.md — Implement dynamic background themes and suggestions.

- **Task 1.1:** Research and select background colors/images for different weather conditions.
- **Task 1.2:** Update `app.py` to change background based on weather data.
- **Task 1.3:** Implement suggestion logic based on weather condition/description.
- **Task 1.4:** Add suggestion label to the Tkinter GUI.
- **Verification:** Run `python app.py` and verify background changes and suggestions for different cities.

## Phase 2: Repository C - 5-Day Forecast (Tkinter)
**Goal:** Display a 5-day forecast in the desktop app.
- **Task 2.1:** Modify API call in `app.py` to fetch forecast data.
- **Task 2.2:** Implement daily grouping logic for the 3-hour forecast data.
- **Task 2.3:** Add UI elements (labels/images) to display 5-day summaries (Icon, Min/Max Temp).
- **Verification:** Search for a city and confirm the 5-day forecast displays correctly.

## Phase 3: Repository B - API Refactor & Frontend Setup
**Goal:** Refactor the Flask app into a JSON API and set up a new React frontend project.
- **Task 3.1 (Backend):** Modify `main.py` in `2025f-feature-development-b` to remove HTML template rendering.
- **Task 3.2 (Backend):** Create a new API endpoint (e.g., `/api/weather/<city>`) that processes data and returns a clean JSON response (including current weather and 5-day forecast).
- **Task 3.3 (Frontend):** Create a new directory for the React application (e.g., `2025f-feature-development-b/frontend`).
- **Task 3.4 (Frontend):** Use Vite to initialize a new React project in the `frontend` directory.
- **Task 3.5 (Frontend):** Install and configure Tailwind CSS for the new React project.
- **Verification:** The Flask API is browsable and returns valid JSON; the new React app runs successfully.

## Phase 4: Repository B - React UI Implementation
**Goal:** Build the weather application's user interface using React and Tailwind CSS.
- **Task 4.1:** Create React components for the main layout, search bar, current weather display, and 5-day forecast cards.
- **Task 4.2:** Implement a service/hook in React to fetch data from the Flask API.
- **Task 4.3:** Manage application state (loading, error, weather data) within React.
- **Task 4.4:** Implement the dynamic background themes and weather-based suggestions on the frontend.
- **Task 4.5:** Style all components using Tailwind CSS to create a polished, responsive UI.
- **Verification:** The web application correctly displays weather data and all features from the requirements are functional.

## Phase 5: Final Review & Polish
**Goal:** Ensure consistency and quality across both applications.
- **Task 5.1:** Conduct a final code review for both repositories.
- **Task 5.2:** Verify error handling for both apps (e.g., city not found).
- **Task 5.3:** Final manual testing for all requirements.
- **Verification:** Both apps run without errors and all features are functional.
