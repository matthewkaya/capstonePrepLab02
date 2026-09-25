# AIGC 5005 Lab 02 - Weather Data Aggregation
# Author Muharrem Kaya

This project downloads hourly weather data from Open-Meteo API for Toronto and makes some daily summaries. The result is saved into a JSON file.

## Data source

Open-Meteo public weather API is used.

The program gets temperature and precipitation data for past 7 days. It normally processes 168 hourly records.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows:

```bash
.venv\Scripts\activate
```

## Run

```bash
python records.py
```

After program runs, it creates:

```text
summary.json
```

## Example output

```json
{
  "records_processed": 168,
  "unique_days": 7,
  "warmest_day": {
    "date": "2026-09-18",
    "temperature": 22.6
  }
}
```

## Data quirks

The API gives time, temperature and precipitation as seperate lists. I used `zip()` to put them together as hourly records.

Some weather values can be missing, so the program skips missing temperature or precipitation values.

During my test, precipitation values was 0.0 for all days.

If the API request fail, program prints a clear message instead of showing traceback.

## Design choices

I used a list for hourly records.

I used dictionaries for grouping weather values by date and for creating the summary.

I used a set for getting unique dates.

I also used a dictionary comprehension when finding the warmest day.

Functions are seperated so each function is doing one main job.

## Known limitations

The location is fixed to Toronto.

The program only checks previous 7 days.

It only calculates daily temperature summary, precipitation totals and warmest day.
