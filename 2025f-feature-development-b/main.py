import datetime
import requests
import string
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from a .env file in the project root
load_dotenv()

# OpenWeather API endpoints
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
OWM_FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
GEOCODING_API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"

# Read the OpenWeather API key from environment variable
api_key = os.getenv("OWM_API_KEY")

# Create the Flask app instance
app = Flask(__name__)
CORS(app) # Enable CORS for all routes

def process_forecast(forecast_list):
    """Group 3-hour intervals into 5 daily summaries (Max/Min Temp, Icon)"""
    by_day = {}
    for item in forecast_list:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        day = dt.strftime('%Y-%m-%d')
        if day not in by_day:
            by_day[day] = []
        by_day[day].append(item)

    daily_summaries = []
    sorted_days = sorted(by_day.keys())
    
    # Skip today if we have enough data for the next 5 days
    start_idx = 1 if len(sorted_days) > 5 else 0
    
    for i in range(start_idx, start_idx + 5):
        if i >= len(sorted_days):
            break
        day = sorted_days[i]
        day_data = by_day[day]
        
        max_temp = max(item['main']['temp_max'] for item in day_data)
        min_temp = min(item['main']['temp_min'] for item in day_data)
        # Get icon from middle of the day entry
        icon = day_data[len(day_data)//2]['weather'][0]['icon']
        day_name = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%a')
        
        daily_summaries.append({
            "day": day_name,
            "date": day,
            "temp_max": round(max_temp),
            "temp_min": round(min_temp),
            "icon": icon,
            "description": day_data[len(day_data)//2]['weather'][0]['main']
        })
    return daily_summaries

@app.route("/api/weather/<city>")
def get_weather_api(city):
    """
    JSON API endpoint for weather data.
    """
    try:
        city_name = string.capwords(city)
        
        # 1. Geocoding
        location_params = {"q": city_name, "appid": api_key, "limit": 1}
        location_response = requests.get(GEOCODING_API_ENDPOINT, params=location_params)
        
        if location_response.status_code != 200:
            return jsonify({"error": f"Geocoding API Error: {location_response.json().get('message', 'Unknown Error')}"}), location_response.status_code
            
        location_data = location_response.json()

        if not location_data or (isinstance(location_data, list) and len(location_data) == 0):
            return jsonify({"error": "City not found"}), 404

        if isinstance(location_data, dict) and location_data.get('cod') and location_data.get('cod') != 200:
             return jsonify({"error": location_data.get('message', 'API Error')}), int(location_data.get('cod'))

        lat = location_data[0]['lat']
        lon = location_data[0]['lon']
        actual_city_name = location_data[0]['name']

        # 2. Current Weather
        weather_params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
        weather_response = requests.get(OWM_ENDPOINT, weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # 3. 5-Day Forecast
        forecast_response = requests.get(OWM_FORECAST_ENDPOINT, weather_params)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        # Consolidate Response
        response = {
            "city": actual_city_name,
            "country": location_data[0].get('country'),
            "current": {
                "temp": round(weather_data['main']['temp']),
                "feels_like": round(weather_data['main']['feels_like']),
                "min_temp": round(weather_data['main']['temp_min']),
                "max_temp": round(weather_data['main']['temp_max']),
                "humidity": weather_data['main']['humidity'],
                "pressure": weather_data['main']['pressure'],
                "visibility": weather_data.get('visibility', 0) // 1000,
                "wind_speed": weather_data['wind']['speed'],
                "main": weather_data['weather'][0]['main'],
                "description": weather_data['weather'][0]['description'],
                "icon": weather_data['weather'][0]['icon'],
                "sunrise": weather_data['sys']['sunrise'],
                "sunset": weather_data['sys']['sunset'],
                "dt": weather_data['dt']
            },
            "forecast": process_forecast(forecast_data['list'])
        }

        return jsonify(response)

    except requests.exceptions.HTTPError as e:
        return jsonify({"error": f"OpenWeather API Error: {str(e)}"}), 502
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

