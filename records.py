import requests


SOURCE_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=43.65"
    "&longitude=-79.38"
    "&hourly=temperature_2m,precipitation"
    "&past_days=7"
    "&forecast_days=0"
    "&timezone=America/Toronto"
)


def fetch_records(url):
    """Download weather data from the API and return it as Python data."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("Unable to download weather data.")
        return None


def main():
    data = fetch_records(SOURCE_URL)

    if data is None:
        return

    print("Weather data downloaded successfully.")


if __name__ == "__main__":
    main()