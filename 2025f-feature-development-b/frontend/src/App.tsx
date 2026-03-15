import React, { useState, useEffect } from 'react';

interface ForecastDay {
  day: string;
  date: string;
  temp_max: number;
  temp_min: number;
  icon: string;
  description: string;
}

interface WeatherData {
  city: string;
  country: string;
  current: {
    temp: number;
    feels_like: number;
    min_temp: number;
    max_temp: number;
    humidity: number;
    pressure: number;
    visibility: number;
    wind_speed: number;
    main: string;
    description: string;
    icon: string;
    sunrise: number;
    sunset: number;
    dt: number;
  };
  forecast: ForecastDay[];
}

const App: React.FC = () => {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState<WeatherData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchWeather = async (searchCity: string) => {
    if (!searchCity) return;
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://localhost:5000/api/weather/${searchCity}`);
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'City not found');
      }
      const data: WeatherData = await response.json();
      setWeather(data);
    } catch (err: any) {
      setError(err.message);
      setWeather(null);
    } finally {
      setLoading(false);
    }
  };

  const getSuggestion = (data: WeatherData) => {
    const main = data.current.main;
    const temp = data.current.temp;
    if (main === 'Rain' || main === 'Drizzle') return "It's raining. Groundbreaking. Grab an umbrella or enjoy the drowned-rat look.";
    if (temp < 10) return "It's freezing. Put on a jacket; hypothermia isn't a fashion statement.";
    if (temp > 30) return "It's a furnace out there. Drink water, or don't—I'm not your life coach.";
    if (main === 'Clear') return "The sun is actually out. Go outside and touch some grass, if you can find any.";
    return `It's a day in ${data.city}. Try not to ruin it.`;
  };

  const getThemeClass = (main: string, icon: string) => {
    if (icon.endsWith('n')) return 'bg-slate-900';
    switch (main) {
      case 'Clear': return 'bg-orange-400';
      case 'Rain': 
      case 'Drizzle':
      case 'Thunderstorm': return 'bg-blue-600';
      case 'Clouds': return 'bg-gray-400';
      case 'Snow': return 'bg-blue-100 text-gray-800';
      default: return 'bg-indigo-500';
    }
  };

  return (
    <div className={`min-h-screen transition-colors duration-500 flex flex-col items-center py-10 px-4 text-white ${weather ? getThemeClass(weather.current.main, weather.current.icon) : 'bg-slate-800'}`}>
      <div className="w-full max-w-md">
        <h1 className="text-4xl font-bold text-center mb-8 drop-shadow-md">Weather App</h1>
        
        <form 
          onSubmit={(e) => { e.preventDefault(); fetchWeather(city); }}
          className="flex gap-2 mb-8"
        >
          <input 
            type="text" 
            placeholder="Search City..." 
            className="flex-1 p-3 rounded-lg text-gray-800 bg-white border border-gray-300 outline-none focus:ring-2 focus:ring-blue-300"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          />
          <button 
            type="submit" 
            className="bg-white/20 hover:bg-white/30 px-6 py-2 rounded-lg font-semibold transition-colors border border-white/30"
          >
            Search
          </button>
        </form>

        {loading && <div className="text-center text-xl animate-pulse">Loading...</div>}
        {error && <div className="bg-red-500/80 p-4 rounded-lg mb-4 text-center">{error}</div>}

        {weather && !loading && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            {/* Current Weather Card */}
            <div className="bg-white/20 backdrop-blur-md rounded-2xl p-8 border border-white/30 mb-6 text-center shadow-xl">
              <h2 className="text-3xl font-bold mb-1">{weather.city}, {weather.country}</h2>
              <p className="opacity-80 text-sm mb-4">
                {new Date(weather.current.dt * 1000).toLocaleDateString([], { weekday: 'long', month: 'long', day: 'numeric' })}
              </p>
              
              <div className="flex items-center justify-center gap-4 mb-4">
                <img 
                  src={`https://openweathermap.org/img/wn/${weather.current.icon}@4x.png`} 
                  alt={weather.current.main}
                  className="w-24 h-24 drop-shadow-lg"
                />
                <div className="text-7xl font-bold">{weather.current.temp}°C</div>
              </div>

              <div className="text-2xl font-semibold mb-2 capitalize">{weather.current.description}</div>
              <p className="bg-white/10 p-3 rounded-xl italic text-lg border border-white/10">
                {getSuggestion(weather)}
              </p>

              <div className="grid grid-cols-2 gap-4 mt-8 pt-6 border-t border-white/20">
                <div className="text-left">
                  <p className="text-xs uppercase opacity-70">Feels Like</p>
                  <p className="text-lg font-bold">{weather.current.feels_like}°C</p>
                </div>
                <div className="text-right">
                  <p className="text-xs uppercase opacity-70">Humidity</p>
                  <p className="text-lg font-bold">{weather.current.humidity}%</p>
                </div>
                <div className="text-left">
                  <p className="text-xs uppercase opacity-70">Wind</p>
                  <p className="text-lg font-bold">{weather.current.wind_speed} m/s</p>
                </div>
                <div className="text-right">
                  <p className="text-xs uppercase opacity-70">Visibility</p>
                  <p className="text-lg font-bold">{weather.current.visibility} km</p>
                </div>
              </div>
            </div>

            {/* 5-Day Forecast */}
            <h3 className="text-xl font-bold mb-4 ml-2">5-Day Forecast</h3>
            <div className="grid grid-cols-5 gap-2">
              {weather.forecast.map((day) => (
                <div key={day.date} className="bg-white/10 backdrop-blur-sm rounded-xl p-3 border border-white/20 text-center flex flex-col items-center">
                  <span className="font-bold text-sm uppercase">{day.day}</span>
                  <img 
                    src={`https://openweathermap.org/img/wn/${day.icon}.png`} 
                    alt={day.description}
                    className="w-10 h-10 my-1"
                  />
                  <div className="text-xs">
                    <span className="font-bold">{day.temp_max}°</span>
                    <span className="opacity-70 ml-1">{day.temp_min}°</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
