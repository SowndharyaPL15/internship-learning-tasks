
import requests

latitude = 11.0168
longitude = 76.9558

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto"
}

try:
    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    current = data["current"]

    print("=" * 40)
    print("       COIMBATORE WEATHER REPORT")
    print("=" * 40)
    print("Time:", current["time"])
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind Speed:", current["wind_speed_10m"], "km/h")
    print("=" * 40)

except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.ConnectionError:
    print("Connection failed. Check your internet connection.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

except (KeyError, TypeError) as error:
    print("Unexpected API response:", error)
