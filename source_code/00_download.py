# downloads the raw data into data/raw, never edits it

import os
import urllib.request

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
