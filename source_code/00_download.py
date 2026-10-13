# downloads the raw data into data/raw, never edits it

import os
import urllib.request
import calendar

import config

def download_file(url, target):
    if os.path.exists(target):
        print("already downloaded, skipped:", target)
        return
    partial = target + ".part"
    urllib.request.urlretrieve(url, partial)
    os.replace(partial, target)
    print("downloaded:", target)


stations_folder = os.path.join(config.RAW_DIR, "stations")
os.makedirs(stations_folder, exist_ok=True)
download_file(config.STATIONS_URL, os.path.join(stations_folder, "stations.csv"))

weather_folder = os.path.join(config.RAW_DIR, "weather")
os.makedirs(weather_folder, exist_ok=True)
for month in config.MONTHS:
    year = int(month[:4])
    month_number = int(month[5:7])
    last_day = calendar.monthrange(year, month_number)[1]
    url = config.WEATHER_URL.format(start=f"{month}-01", end=f"{month}-{last_day:02d}")
    download_file(url, os.path.join(weather_folder, f"weather_{month}.csv"))
