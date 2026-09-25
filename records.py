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


def build_hourly_records(data):

    """Combine hourly weather lists into a list of weather records."""

    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]
    precipitation = data["hourly"]["precipitation"]
    records = []

    for time, temperature, rain in zip(times, temperatures, precipitation):
        record = {
            "time": time,
            "temperature": temperature,
            "precipitation": rain
        }

        records.append(record)

    return records

def group_temperatures_by_day(records):
    """Group temperature values by date."""
    daily_temperatures = {}

    for record in records:
        date = record["time"].split("T")[0]
        temperature = record["temperature"]

        if temperature is None:
            continue

        if date not in daily_temperatures:
            daily_temperatures[date] = []

        daily_temperatures[date].append(temperature)

    return daily_temperatures

def main():
    data = fetch_records(SOURCE_URL)

    if data is None:
        return

    records = build_hourly_records(data)
    daily_temperatures = group_temperatures_by_day(records)

    print("Number of hourly records:", len(records))
    print("Number of days:", len(daily_temperatures))

    for date, temperatures in daily_temperatures.items():
        print(date, temperatures)


if __name__ == "__main__":
    main()