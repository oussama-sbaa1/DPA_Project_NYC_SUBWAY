# downloads the raw data into data/raw, never edits it

import os
import urllib.request
import calendar
import json
import urllib.parse

import config

def download_file(url, target):
    if os.path.exists(target):
        print("already downloaded, skipped:", target)
        return
    partial = target + ".part"
    urllib.request.urlretrieve(url, partial)
    os.replace(partial, target)
    print("downloaded:", target)

def download_ridership_month(month, folder):
    target = os.path.join(folder, f"ridership_{month}.csv")
    if os.path.exists(target):
        print("already downloaded, skipped:", target)
        return

    # which dataset, and which time range (the whole month)
    dataset = config.ridership_dataset_for(month)
    year = int(month[:4])
    month_number = int(month[5:7])
    last_day = calendar.monthrange(year, month_number)[1]
    where = (f"transit_timestamp >= '{month}-01T00:00:00' AND "
             f"transit_timestamp <= '{month}-{last_day:02d}T23:59:59'")

    # 1. ask the API how many rows to expect
    count_query = urllib.parse.urlencode({"$select": "count(*) AS n", "$where": where})
    count_url = config.RIDERSHIP_API.format(dataset=dataset) + ".json?" + count_query
    expected = int(json.load(urllib.request.urlopen(count_url))[0]["n"])
    print(month, ": expecting", expected, "rows from dataset", dataset)

    # 2. download page after page into the .part file
    partial = target + ".part"
    with open(partial, "wb") as out:
        offset = 0
        while offset < expected:
            page_query = urllib.parse.urlencode({"$where": where, "$order": ":id",
                                                 "$limit": config.PAGE_SIZE, "$offset": offset})
            page_url = config.RIDERSHIP_API.format(dataset=dataset) + ".csv?" + page_query
            response = urllib.request.urlopen(page_url)
            header = response.readline()
            if offset == 0:
                out.write(header)
            out.write(response.read())
            offset = offset + config.PAGE_SIZE
            print("   ", month, ":", min(offset, expected), "/", expected)

    # 3. check: one header line + one line per row
    with open(partial, "rb") as f:
        rows = sum(1 for line in f) - 1
    if rows != expected:
        raise RuntimeError(f"{month}: got {rows} rows, expected {expected}")
    os.replace(partial, target)
    print("downloaded:", target, "-", rows, "rows")


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

ridership_folder = os.path.join(config.RAW_DIR, "ridership")
os.makedirs(ridership_folder, exist_ok=True)
for month in config.MONTHS[:1]:
    download_ridership_month(month, ridership_folder)