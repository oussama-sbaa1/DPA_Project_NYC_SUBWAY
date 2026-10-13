# config.py – the months, the data folder, the download sources.

MONTHS = [
    "2024-07",
    "2024-08",
    "2024-09",
    "2024-10",
    "2024-11",
    "2024-12",
    "2025-01",
    "2025-02",
    "2025-03",
    "2025-04",
    "2025-05",
    "2025-06",
]

RAW_DIR = "data/raw"


STATIONS_URL = "https://data.ny.gov/api/views/39hk-dx4f/rows.csv?accessType=DOWNLOAD"

# The MTA publishes hourly ridership as one dataset per period:
# our window (Jul 2024 - Jun 2025) needs both of them.
def ridership_dataset_for(month):
    if month < "2025-01":
        return "wujg-7c2s"   # months up to Dec 2024: dataset "MTA Subway Hourly Ridership: 2020-2024"
    else:
        return "5wq4-mkjj"   # months from Jan 2025: dataset "MTA Subway Hourly Ridership: Beginning 2025"

