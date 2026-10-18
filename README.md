# Project title : Critical Stations and Live Disruptions in the New York City Subway



## Domain : public transport, the New York City subway: critical stations and live disruptions



## Main question : Which subway stations are critical for the network, and are live disruptions happening in those stations or not?



## Sub-questions

* Part 1 (Volume): What is the usual ridership in each subway station by hour and day of the week, and

by how much does the weather change it?

* Part 2 (Velocity): Right now, which stations have live alerts for disruptions, and how busy

are those stations normally at this hour?

* Part 3 (Variety): Which stations are the most central in the New York subway network, and are

those central stations also the busiest ones?



## Team : Oussama Sbaa / Mazen Morsy / Abdullah Hameed







* Part 1: How To Reproduce the whole Pileline ? 

&#x20;Requirements: Docker Desktop with an allowance of at least 6GB of memory, About 15GB of free space in your disk (5GB for data + The docker image) , Internet connection. 



1/ Get the repository content from git: 

git clone https://github.com/oussama-sbaa1/DPA\_Project\_NYC\_SUBWAY.git

cd DPA\_Project\_NYC\_SUBWAY



2/ Start the environment: docker compose up -d --build



3/ Run the notebooks in this Order : 

| # | Notebook | What it does | Time | Check |

| 1 | `00\_download.ipynb` | the script that downloads the raw data from the MTA and NOAA into `data/raw` (CSV, 5.1 GB) | 20–40 min | 12 ridership months, 12 weather files, 1 stations file |

| 2 | `01\_ingest.ipynb` | reads the CSV files with explicit schemas, writes typed Parquet (`data/bronze`) | 3–5 min | 29,375,687 rows / 496 rows/ 11,765 rows |

| 3 | `02\_clean.ipynb` | 12 cleaning rules → clean tables (`data/silver`) + `results/cleaning\_report.csv` | \~4 min | 3,620,146 rows / 445 rows / 8,704 rows |

| 4 | `03\_analyze\_stations.ipynb` | usual ridership per station, day and hour + busiest stations (`data/gold`) + 2 figures | \~2 min | Times Sq-42 St first, ≈ 129,777 riders per day |

| 5 | `04\_analyze\_weather.ipynb` | effect of rain and snow on ridership (`data/gold`) + 2 figures | \~1 min | light rain −2.0 %, heavy rain −1.0 %, snow −4.8 % |



For each notebook in the kernel menu click Kernel → Restart Kernel and Run All Cells, wait until it is finished,

then in the Kernel menu click Kernel → Shut Down All Kernels before opening the next one.



4/ Results : The cleaning report is written in report/Cleaning\_Report. The result tables (CSV) and 4 figures (in `results/figures/`) are written to `results/`



5/ Stop : docker compose down





Repository structure

\- `source_code/`: the notebooks explore\_one\_month.ipynb which is our first exploration of July 2024, 00\_download.ipynb, 01\_ingest.ipynb, 02\_clean.ipynb, 03\_analyse\_station.ipynb, 04\_analyse weather.ipynb

\- `documentation/`: the proposal NYC\_Subway\_Proposal\_OnePage and problems\_log.md containing the data problems we found

\- `results/`: result tables and figures

\- `report/`: the cleaning report and the final delivery report for part 1 : NYC\_Subway\_Part1\_Delivrable\_Report

\- `data/`: created by the notebooks, it doesn't exist on GitHub (5 GB) it is created in order to put the raw downloaded data, the bronze, silver and gold layer parquet files. 



Data sources and licences

| Dataset | Source | Licence |

|---|---|---|

| MTA Subway Hourly Ridership 2020–2024 and Beginning 2025 | data.ny.gov/d/wujg-7c2s · data.ny.gov/d/5wq4-mkjj | OPEN-NY Terms of Use |

| MTA Subway Stations | data.ny.gov/d/39hk-dx4f | OPEN-NY Terms of Use |

| NOAA Local Climatological Data v2, Central Park (USW00094728) | ncei.noaa.gov | U.S. public domain, cite NOAA |



















