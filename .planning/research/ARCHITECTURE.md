# Architecture Patterns: Weather App Integration

**Project:** Weather App Challenge
**Researched:** 2024-10-27
**Confidence:** HIGH

## Recommended Architecture: Flask-to-OpenWeather-Bridge

The system uses a **Backend-Driven Data Processing** pattern. Instead of passing raw OpenWeather JSON directly to the frontend, Flask handles the logic of grouping 40 intervals into 5 days.

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| Flask Route (`/forecast`) | Orchestrates the request, extracts city name, calls the API. | OpenWeather API |
| Weather Service Layer | Groups 40 forecast points into 5 summaries (Max/Min calculation). | Flask Route, API Response |
| Asset Mapper | Maps `weather[0].main` strings to local `/static/assets/*.png` paths. | Flask Logic |
| Jinja2 Template | Loops over the 5-day list and renders the HTML cards. | Client Browser |

### Data Flow

1. Client sends a request to `/forecast?city=London`.
2. Flask fetches the raw 40-item `list` from OpenWeather.
3. Flask groups items by the `dt_txt` date string.
4. For each day, it calculates:
   - `max(temp)` and `min(temp)`.
   - Selects one `description` and `icon` (typically from the midday slot).
5. The processed list of 5 objects is passed to the Jinja2 template.

## Patterns to Follow

### Pattern 1: Midday Forecast Selection
For a clean 5-day view, use the 12:00:00 (midday) forecast as the representative for that day's main icon and description.

**Example Logic:**
```python
def get_daily_summaries(forecast_list):
    days = {}
    for item in forecast_list:
        # Extract date and time
        dt = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
        date_str = dt.strftime("%Y-%m-%d")
        
        if date_str not in days:
            days[date_str] = {"temps": [], "main": "", "desc": ""}
            
        days[date_str]["temps"].append(item['main']['temp'])
        
        # Select midday as representative (roughly 12:00:00)
        if dt.hour == 12:
            days[date_str]["main"] = item['weather'][0]['main']
            days[date_str]["desc"] = item['weather'][0]['description']
            
    return days
```

### Pattern 2: Icon Mapping Utility
Use a mapping dictionary to link OpenWeather's `main` weather category to local assets.

| OpenWeather `main` | Local Asset Path |
|-------------------|------------------|
| "Clear" | `/static/assets/clear.png` |
| "Clouds" | `/static/assets/clouds.png` |
| "Rain" | `/static/assets/rain.png` |
| "Thunderstorm" | `/static/assets/thunderstorm.png` |
| "Drizzle" | `/static/assets/drizzle.png` |
| "Snow" | `/static/assets/snow.png` |
| "Mist"/"Fog"/"Haze" | `/static/assets/mist.png` (or respective asset) |

## Anti-Patterns to Avoid

### Anti-Pattern 1: Frontend Grouping
**What:** Sending all 40 data points to the browser and grouping with JavaScript.
**Why bad:** Bloats the payload (40 objects vs 5), increases client-side CPU, and complicates templates.
**Instead:** Process data in Flask so the frontend only receives what it needs to display.

### Anti-Pattern 2: Hardcoding Icons in HTML
**What:** Using `if condition == 'Rain'` inside the Jinja2 HTML file.
**Why bad:** Difficult to maintain if assets or API names change.
**Instead:** Map the asset name in the Python logic and pass the final `icon_path` to the template.

## Scalability Considerations

| Concern | Solution |
|---------|----------|
| API Latency | Implement a simple cache (e.g., `flask-caching`) to store city forecasts for 10-15 minutes. |
| Rate Limits | Monitor the 60 calls/minute limit of the Free tier. Avoid redundant calls on every refresh. |

## Sources

- [Flask Pattern: Using a Service Layer](https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/)
- [OpenWeather JSON Response Format](https://openweathermap.org/forecast5#JSON)
