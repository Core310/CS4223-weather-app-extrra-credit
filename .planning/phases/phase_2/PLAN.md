---
phase: 02-5-day-forecast-repo-c
plan: 01
type: execute
wave: 1
depends_on: [01-base-features-repo-c]
files_modified: [2025f-feature-development-c/app.py]
autonomous: true
requirements: [FR2.1, FR2.2, FR2.4]

must_haves:
  truths:
    - "The app fetches 5-day forecast data in a separate thread."
    - "The forecast is displayed in a horizontal scrollable or fixed area."
    - "Each forecast day shows the Day of Week, Weather Icon, Min Temp, and Max Temp."
  artifacts:
    - path: "2025f-feature-development-c/app.py"
      provides: "Forecast UI and logic"
---

<objective>
Extend the Tkinter desktop application (Repository C) to display a 5-day weather forecast. This involves fetching data from the OpenWeather 5-day/3-hour forecast API, processing it to group into daily summaries, and updating the UI with new components to show the forecast cards.
</objective>

<tasks>

<task type="auto">
  <name>Task 1: Implement Forecast Data Fetching and Processing</name>
  <files>2025f-feature-development-c/app.py</files>
  <action>
    - Modify `__get_weather` to also call `__get_forecast`.
    - Implement `__get_forecast(self)` to fetch data from `https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api}`.
    - Implement `__process_forecast(self, data)` to group the 3-hour chunks into 5 daily summaries. For each day, find the weather icon, min temp, and max temp from the 8 chunks (24 hours).
  </action>
</task>

<task type="auto">
  <name>Task 2: Build Forecast UI Components</name>
  <files>2025f-feature-development-c/app.py</files>
  <action>
    - In `__gui`, create a container frame (e.g., `self.forecast_frame`) at the bottom of the window (adjusting existing layouts if needed, or making the window taller).
    - Create a list to store forecast UI elements (labels for day, icon, temps) to easily update or clear them.
    - Implement a method `update_forecast_ui(self, forecast_data)` to populate the frame with the processed data.
  </action>
</task>

<task type="auto">
  <name>Task 3: Integration and Refinement</name>
  <files>2025f-feature-development-c/app.py</files>
  <action>
    - Ensure `update_theme` also updates the background of the new forecast elements.
    - Update `clear` to reset the forecast display.
    - Handle loading states or errors specifically for the forecast API call.
  </action>
</task>

</tasks>

<success_criteria>
- Searching for a city displays both the current weather and a 5-day forecast.
- Each forecast day is clearly labeled with the day of the week, an icon, and high/low temperatures.
- The UI remains responsive during data fetching.
</success_criteria>
