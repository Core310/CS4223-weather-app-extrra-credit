---
phase: 01-base-features-repo-c
plan: 01
type: execute
wave: 1
depends_on: []
files_modified: [2025f-feature-development-c/app.py]
autonomous: true
requirements: [FR1.2, FR3.1]

must_haves:
  truths:
    - "Background color changes when weather data is fetched."
    - "Suggestion message is displayed near the temperature label."
    - "All visible labels have consistent background colors with the root window."
  artifacts:
    - path: "2025f-feature-development-c/app.py"
      provides: "Dynamic background and suggestions implementation"
  key_links:
    - from: "2025f-feature-development-c/app.py:__set_information"
      to: "2025f-feature-development-c/app.py:update_theme"
      via: "method call"
---

<objective>
Implement dynamic background themes and weather-based suggestions for the Tkinter desktop application (Repository C). This involves updating the UI based on weather conditions and temperature, ensuring a consistent look and feel.
</objective>

<execution_context>
@/home/arika/.gemini/get-shit-done/workflows/execute-plan.md
@/home/arika/.gemini/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/STATE.md
@.planning/REQUIREMENTS.md
@2025f-feature-development-c/app.py

<interfaces>
From 2025f-feature-development-c/app.py:
```python
class Weather(Tk):
    def __init__(self): ...
    def __gui(self): ...
    def __get_weather(self): ...
    def __set_information(self, weather): ...
```
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Define Theme Mapping and Initialize Suggestion Label</name>
  <files>2025f-feature-development-c/app.py</files>
  <action>
    - Define a `WEATHER_THEMES` constant (dictionary) at the top of the file mapping weather condition keys (Clear, Clouds, Rain, Snow, Thunderstorm, Drizzle, Haze, Mist) to hex colors and default suggestion strings.
    - In the `__gui` method of the `Weather` class, initialize a new `self.suggestion` Label widget. 
    - Position it below the temperature and 'feels like' labels (e.g., around x=280, y=280) using the `place` method.
    - Ensure it has a readable font (e.g., "Nirmala UI", 12, "italic").
  </action>
  <verify>
    <automated>grep -q "WEATHER_THEMES" 2025f-feature-development-c/app.py && grep -q "self.suggestion =" 2025f-feature-development-c/app.py</automated>
  </verify>
  <done>Theme mapping exists and suggestion label is initialized in the GUI.</done>
</task>

<task type="auto">
  <name>Task 2: Implement Theme Update Logic and Suggestion Generation</name>
  <files>2025f-feature-development-c/app.py</files>
  <action>
    - Add a method `update_theme(self, color)` to the `Weather` class. This method should:
        1. Update `self.config(bg=color)`.
        2. Iterate over all child widgets and update their `bg` attribute to `color` if they are Labels (excluding the bottom bar labels which have `bg='#00b7ff'`).
    - Modify `__set_information(self, weather)` to:
        1. Extract the main weather condition and current temperature (Celsius).
        2. Determine the theme color and initial suggestion from `WEATHER_THEMES`.
        3. Apply temperature-based overrides to the suggestion (e.g., < 10°C or > 30°C as per FR3.1).
        4. Call `self.update_theme(color)`.
        5. Update `self.suggestion['text']` with the final message.
    - Update `clear(self)` to reset the background color to the default and clear the suggestion label text.
  </action>
  <verify>
    <automated>grep -q "def update_theme" 2025f-feature-development-c/app.py && grep -q "self.update_theme" 2025f-feature-development-c/app.py</automated>
  </verify>
  <done>The app dynamically updates themes and suggestions based on weather data.</done>
</task>

<task type="auto">
  <name>Task 3: Verification Script and Manual Test Plan</name>
  <files>2025f-feature-development-c/verify_ui.py</files>
  <action>
    - Create a small verification script `2025f-feature-development-c/verify_ui.py` that imports the `Weather` class (if possible, or just lists manual verification steps).
    - Since Tkinter is graphical, the primary verification is manual. Include instructions in the script or a comment:
        1. Run `python 2025f-feature-development-c/app.py`.
        2. Search for a sunny city (e.g., "Phoenix") and verify the golden theme.
        3. Search for a rainy city (e.g., "London") and verify the blue/gray theme.
        4. Search for a very cold or hot city and verify the specific suggestion message.
  </action>
  <verify>
    <automated>ls 2025f-feature-development-c/verify_ui.py</automated>
  </verify>
  <done>Verification steps are documented and ready for manual testing.</done>
</task>

</tasks>

<verification>
Check for the following:
1. `WEATHER_THEMES` mapping is comprehensive.
2. `update_theme` method handles multiple widgets correctly.
3. `__set_information` integrates theme and suggestion logic seamlessly.
</verification>

<success_criteria>
- The Tkinter application background changes color based on the searched city's weather.
- A suggestion message relevant to the current weather and temperature is displayed.
- The UI remains consistent with updated label backgrounds.
</success_criteria>

<output>
After completion, create `.planning/phases/phase_1/01-01-SUMMARY.md`
</output>
