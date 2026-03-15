# Weather App Challenge Technical Report

**Student Name:** [Your Name]
**Student ID:** [Your Student ID]
**Project Title:** Multi Platform Weather System Extensions for Repo B and Repo C

## Project Overview
This project involved extending two different weather applications with new features. Repository C is a desktop app built with Tkinter, and Repository B is a web app built with Flask. The main goals were to add dynamic themes, 5 day forecasts, and context aware suggestions for both platforms while following Category 4 requirements.

## Requirements Mapping
The following features were implemented and verified based on the requirements document.

| Requirement | Implementation Status |
|:---|:---|
| Dynamic Background Themes | Finished. React uses Tailwind classes and Tkinter uses recursive updates. |
| 5 Day Forecast Extension | Finished. Data is fetched from OpenWeather and processed into daily summaries. |
| Weather Based Suggestions | Finished. Personality driven engine added to both user interfaces. |

## Repository File Layouts

### Repository C (Desktop App)
The desktop app is a standalone Python project using Tkinter.

*   `app.py`: Main entry point handling the user interface and API calls
*   `config.ini`: Secure storage for the API key
*   `requirements.txt`: Python packages like requests and Pillow
*   `verify_ui.py`: Manual test plan for visual validation
*   `Icons/`: Weather specific icons for the UI
*   `Images/`: UI assets like borders and backgrounds

### Repository B (Web App)
The web app uses a decoupled architecture with a Python backend and React frontend.

*   `main.py`: Flask JSON API that aggregates weather data
*   `requirements.txt`: Backend packages like Flask and Flask CORS
*   `.env`: Environment variables for the API key
*   `frontend/src/App.tsx`: Main React component for state and UI
*   `frontend/src/index.css`: Tailwind CSS entry point
*   `frontend/vite.config.ts`: Build config for Vite

## Technical Implementation

### Dynamic Theme Mapping (React)
This code shows how background colors change based on weather and night detection.

```typescript
const getThemeClass = (main: string, icon: string) => {
  if (icon.endsWith('n')) return 'bg-slate-900'
  
  switch (main) {
    case 'Clear': return 'bg-orange-400'
    case 'Rain': 
    case 'Drizzle':
    case 'Thunderstorm': return 'bg-blue-600'
    case 'Clouds': return 'bg-gray-400'
    case 'Snow': return 'bg-blue-100 text-gray-800'
    default: return 'bg-indigo-500'
  }
}
```

### Recursive UI Update (Tkinter)
The desktop app needs to loop through all widgets to update backgrounds correctly.

```python
def update_theme(self, color):
    self.config(bg=color)
    if hasattr(self, 'forecast_frame'):
        self.forecast_frame.config(bg=color)
        for child in self.forecast_frame.winfo_children():
            if isinstance(child, (Frame, Label)):
                child.config(bg=color)
                for gchild in child.winfo_children():
                    if isinstance(gchild, (Frame, Label)):
                        gchild.config(bg=color)
```

### Snarky Suggestion Engine
The app provides personality driven advice instead of generic messages.

```typescript
const getSuggestion = (data: WeatherData) => {
  const temp = data.current.temp
  if (temp < 10) return "It's freezing. Put on a jacket; hypothermia isn't a fashion statement"
  if (temp > 30) return "It's a furnace out there. Drink water, or don't—I'm not your life coach"
}
```

## Architecture and Engineering

### Decoupled Web Architecture
The Flask app was refactored from a monolithic app into a JSON API. The frontend is a React app built with Vite and Tailwind CSS. This decoupling makes the system more maintainable and faster.

### Stability Improvements
The desktop app had some threading issues that were fixed by keeping UI logic on the main thread. Memory leaks were also resolved by reusing existing widgets during updates.

## Testing and Verification

### Test Specification
Tests followed a simple model: give a city, trigger a search, and verify the UI looks right.

### Verification Suites
*   **Thermal Checks:** Confirmed that suggestions change at the right temperature points
*   **Visual Checks:** Verified icons load from the CDN and night mode triggers correctly
*   **Error Checks:** Verified that invalid cities show clear feedback without crashing

## Conclusion
The system now meets all challenge requirements. By using a decoupled web architecture and fixing the desktop app stability, we created a robust weather suite that is fun to use with its snarky suggestions and dynamic themes.
