def run(state):
    """Fetch weather data from OpenWeatherMap API or use simulated data in test mode"""
    # Check if we're in test mode (indicated by pre-populated weather_data)
    if state['weather_data']:
        return {
            **state,
            "messages": state["messages"] + [SystemMessage(content=f"Using simulated weather data for {state['city']}")]
        }

    # If not in test mode, fetch real data from API
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = os.getenv("API_KEY")

    request_url = f"{BASE_URL}?appid={API_KEY}&q={state['city']}"
    try:
        response = requests.get(request_url)
        response.raise_for_status()

        data = response.json()
        weather_data = {
            "weather": data.get('weather', [{}])[0].get("description", "N/A"),
            "wind_speed": data.get("wind", {}).get("speed", "N/A"),
            "cloud_cover": data.get("clouds", {}).get("all", "N/A"),
            "sea_level": data.get("main", {}).get("sea_level", "N/A"),
            "temperature": round(data.get("main", {}).get("temp", 273.15) - 273.15, 1),
            "humidity": data.get("main", {}).get("humidity", "N/A"),
            "pressure": data.get("main", {}).get("pressure", "N/A")
        }

        return {
            **state,
            "weather_data": weather_data,
            "messages": state["messages"] + [SystemMessage(content=f"Weather data fetched successfully for {state['city']}")]
        }
    except Exception as e:
        error_data = {
            "weather": "N/A",
            "wind_speed": "N/A",
            "cloud_cover": "N/A",
            "sea_level": "N/A",
            "temperature": "N/A",
            "humidity": "N/A",
            "pressure": "N/A"
        }
        return {
            **state,
            "weather_data": error_data,
            "messages": state["messages"] + [SystemMessage(content=f"Failed to fetch weather data for {state['city']}: {str(e)}")]
        }