# Domain Pitfalls: Weather App Integration

**Project:** Weather App Challenge
**Researched:** 2024-10-27
**Confidence:** HIGH

## Critical Pitfalls

Mistakes that cause rewrites or major issues.

### Pitfall 1: Timezone Misalignment (UTC vs. Local Time)
**What goes wrong:** The API returns `dt_txt` in UTC. If it is 11 PM UTC, the data point belongs to "today" in London but "tomorrow" in Tokyo.
**Why it happens:** The 5-day forecast API does not automatically adjust for the city's timezone in the `dt_txt` field.
**Consequences:** Forecast days can appear shifted by 1 (showing Monday's forecast on Tuesday morning) or showing duplicate days.
**Prevention:** Use the `timezone` offset (in seconds) provided in the `city` object of the response to calculate the local time for each data point.
**Detection:** Check if the first day in the forecast matches the user's current local date.

### Pitfall 2: Confusing 3-Hour Temps with Daily Highs/Lows
**What goes wrong:** Displaying the `temp_max` from a single 3-hour window as the daily high.
**Why it happens:** `main.temp_max` in the 5-day/3-hour API is the maximum temperature *during that 3-hour period*, not the whole day.
**Consequences:** Users see a "Daily High" of 18°C when the actual high at noon was 24°C.
**Prevention:** Iterate through all 8 entries for a single day and find the absolute maximum and minimum `temp` across all of them.

## Moderate Pitfalls

### Pitfall 1: Missing Assets for Edge Case Weather
**What goes wrong:** The API returns "Squall" (771) or "Ash" (762), but the app only has icons for "Rain" and "Clear".
**Prevention:** Use a default fallback icon (e.g., `clouds.png`) for any weather ID that doesn't have a direct mapping in your local assets folder.

### Pitfall 2: API Rate Limiting (Free Tier)
**What goes wrong:** App crashes or shows 401/429 errors when multiple users search simultaneously.
**Prevention:** Implement basic error handling in Flask for non-200 responses and cache results for popular cities.

## Minor Pitfalls

### Pitfall 1: Units Inconsistency
**What goes wrong:** API defaults to Kelvin (Standard). The app shows "298°" which confuses users in the US/UK.
**Prevention:** Always append `&units=metric` or `&units=imperial` to the API request URL based on project requirements.

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Data Integration | JSON parsing error if city is not found. | Wrap API call in try-except and check for `cod == 200`. |
| UI/UX | Horizontal overflow on mobile for 5 cards. | Ensure responsive CSS (flex-wrap) for the forecast list. |

## Sources

- [OpenWeather API Forum: 5-day forecast grouping](https://openweathermap.org/faq#forecast)
- [Python Datetime Timezone Handling](https://docs.python.org/3/library/datetime.html#timezone-objects)
