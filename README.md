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


## Part 1: How to Reproduce the Entire Pipeline

### Prerequisites

Before running the project, ensure you have:

- **Docker Desktop** installed, with at least **6 GB of memory** allocated.
- **15 GB of free disk space** (approximately 5 GB for the raw datasets and additional space for Docker images and processed data).
- A stable **internet connection** to download the datasets.

### Step 1: Clone the GitHub Repository

Open a terminal and execute:

```bash
git clone https://github.com/oussama-sbaa1/DPA_Project_NYC_SUBWAY.git
cd DPA_Project_NYC_SUBWAY
```

### Step 2: Start the Docker Environment

Build and start the Docker containers:

```bash
docker compose up -d --build
```

### Step 3: Execute the Notebooks

Run the following notebooks **in the specified order**:

| # | Notebook | Description | Estimated Time | Expected Output / Verification |
|---|---|---|---|---|
| 1 | `00_download.ipynb` | Downloads the raw MTA and NOAA datasets into `data/raw` (approximately 5.1 GB). | 20–40 min | 12 ridership CSV files, 12 weather CSV files, and 1 stations CSV file |
| 2 | `01_ingest.ipynb` | Reads CSV files using explicit schemas and converts them into typed Parquet files (`data/bronze`). | 3–5 min | 29,375,687 ridership rows, 496 station rows, and 11,765 weather rows |
| 3 | `02_clean.ipynb` | Applies cleaning rules and generates cleaned datasets (`data/silver`) and `results/cleaning_report.csv`. | ~4 min | 3,620,146 station-hour rows, 445 station complexes, and 8,704 weather-hour rows |
| 4 | `03_analyze_stations.ipynb` | Calculates usual ridership by station, weekday, and hour; identifies the busiest stations; and generates two figures. | ~2 min | Times Sq–42 St ranked first, with approximately 129,777 riders per day |
| 5 | `04_analyze_weather.ipynb` | Analyzes the association between rain, snow, and subway ridership; generates two figures. | ~1 min | Light rain: −2.0%, heavy rain: −1.0%, snow: −4.8% |

**Notebook execution instructions:**

1. Open the notebook in Jupyter.
2. Select **Kernel → Restart Kernel and Run All Cells**.
3. Wait until all cells finish executing.
4. Select **Kernel → Shut Down All Kernels** before opening the next notebook.
5. Repeat until all five notebooks have been executed.

> **Note:** Execution times are approximate and depend on your computer's hardware, available memory, and internet connection.

### Step 4: View the Results

After the pipeline completes, the following outputs are available:

- **Cleaning report:** `report/Cleaning_Report`
- **Result tables (CSV):** `results/`
- **Generated figures:** `results/figures/`
- **Processed Parquet datasets:** `data/bronze/`, `data/silver/`, and `data/gold/`

The analysis generates four figures illustrating subway ridership patterns and weather-associated changes.

### Step 5: Stop the Docker Environment

When finished, stop and remove the running containers:

```bash
docker compose down
```

---

## Repository Structure

The repository is organized into the following directories:

- **`source_code/`** — Jupyter notebooks containing the implementation:
  - `explore_one_month.ipynb` — Initial exploration of July 2024 ridership data.
  - `00_download.ipynb` — Downloads the raw datasets.
  - `01_ingest.ipynb` — Ingests CSV files and creates Bronze-layer Parquet tables.
  - `02_clean.ipynb` — Cleans and transforms the datasets into Silver-layer tables.
  - `03_analyze_stations.ipynb` — Analyzes station ridership patterns.
  - `04_analyze_weather.ipynb` — Analyzes weather-associated ridership changes.

- **`documentation/`** — Project documentation:
  - `NYC_Subway_Proposal_OnePage` — Initial project proposal.
  - `problems_log.md` — Documented data-quality issues and observations.

- **`results/`** — Generated analysis tables and visualizations.
  - `figures/` — Four generated figures.

- **`report/`** — Project deliverables:
  - `Cleaning_Report` — Cleaning report.
  - `NYC_Subway_Part1_Delivrable_Report` — Final Part 1 report.

- **`data/`** — Generated locally during pipeline execution (not stored on GitHub because of its size):
  - `raw/` — Original downloaded CSV files.
  - `bronze/` — Ingested datasets stored as typed Parquet.
  - `silver/` — Cleaned datasets ready for analysis.
  - `gold/` — Processed analytical datasets.

> **Important:** The `data/` directory is generated during execution and is not included in the GitHub repository.









Data sources and licences

| Dataset | Source | Licence |
|---|---|---|
| MTA Subway Hourly Ridership 2020–2024 and Beginning 2025 | data.ny.gov/d/wujg-7c2s · data.ny.gov/d/5wq4-mkjj | OPEN-NY Terms of Use |
| MTA Subway Stations | data.ny.gov/d/39hk-dx4f | OPEN-NY Terms of Use |
| NOAA Local Climatological Data v2, Central Park (USW00094728) | ncei.noaa.gov | U.S. public domain, cite NOAA |



















