# CS4223 Spring 2026 Weather App Challenge - Implementation Report

**Student Name:** [Your Name]
**Student ID:** [Your Student ID]
**Project Title:** Weather Application Extensions (Repo B & Repo C)

## Overview
This report describes the features implemented for the CS4223 Extra Point - 2 challenge. As per Category 4 instructions, Repository C (Tkinter) and Repository B (Flask/React) were extended with dynamic themes, 5-day forecasts, and weather-based suggestions.

## Implemented Features

### 1. Dynamic Background Themes
Both applications now feature a dynamic user interface that changes its background color/theme based on the current weather condition or time of day.
- **Mappings:**
  - **Sunny/Clear:** Bright/Warm themes (Golden for Tkinter, Orange-400 for React).
  - **Rainy/Stormy:** Gray/Blue themes.
  - **Cloudy:** Neutral/Muted themes.
  - **Night:** Dark theme (applied when the weather icon indicates night time).
- **Implementation Detail:** In Repository B, Tailwind CSS utility classes are applied dynamically. In Repository C, a custom `update_theme` method recursively updates the background of all UI components.

### 2. 5-Day Forecast Extension
A detailed 5-day forecast has been added to both applications, displayed below the current weather section.
- **Data Processing:** The applications fetch data from the OpenWeather 5-day/3-hour forecast API. This data is then grouped into daily summaries.
- **Display Components:** Each forecast day includes:
  - Day of the week (e.g., "Mon").
  - Weather icon representing the middle-of-day condition.
  - High (Max) and Low (Min) temperatures.
- **UI Implementation:** Repo C uses a horizontal grid of frames, while Repo B uses a responsive Flexbox/Grid layout.

### 3. Weather-Based Suggestions
A context-aware suggestion message is displayed to the user based on real-time weather data.
- **Logic:**
  - **Rain:** "It's raining - don't forget an umbrella."
  - **Cold (< 10°C):** "Cold weather today - wear a jacket."
  - **Hot (> 30°C):** "Stay hydrated, it's quite hot outside."
  - **Clear:** "Perfect weather for a walk."
- **Placement:** Displayed prominently below the current temperature to provide immediate value to the user.

## Technical Improvements (Extra)
- **Repo C Refactoring:** Fixed threading issues where GUI initialization was accidentally moved out of the main thread.
- **Repo C Asset Management:** Corrected case-sensitive file naming for Linux compatibility (`Haze.png`) and optimized icon loading to prevent memory leaks.
- **Repo B Architecture:** Refactored the Flask app into a clean JSON API, decoupling the backend logic from the frontend presentation.
- **Modern Tech Stack (Repo B):** Bootstrapped the new frontend using **Vite** and **React (TypeScript)** with **Tailwind CSS v4**.

## Conclusion
All requirements from the challenge PDF have been met and verified. The applications are now more interactive, informative, and visually engaging.
