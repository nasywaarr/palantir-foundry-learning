# 🛠️ Palantir Foundry — Learning & Prep

> Pre-hackathon preparation for **Hack4Future Sicily 2025**
> Platform: [Palantir AIP / Open Data Playground](https://www.palantir.com/platforms/foundry/)

---

## About

This repository documents my hands-on preparation with **Palantir Foundry** ahead of Hack4Future Sicily 2025 — an inter-university hackathon across Sicily focused on data-driven innovation.

Over ~4 weeks, I worked through 10 structured learning modules on the Open Data Playground, building real pipelines, writing Python Transforms, and exploring Foundry's full data engineering stack end-to-end.

---

## Modules Completed

| # | Module | Last Updated |
|---|--------|-------------|
| 1 | Speedrun: Your First E2E Workflow | Mar 31, 2025 |
| 2 | Deep Dive: Building your first Pipeline | Mar 31, 2025 |
| 3 | No-code approach to data cleaning with Pipeline Builder | Apr 2, 2025 |
| 4 | Deep Dive: Data Analysis in Quiver | Apr 17, 2025 |
| 5 | Parse different data formats in Pipeline Builder | Apr 18, 2025 |
| 6 | Deep Dive: Data Analysis with Contour | Apr 23, 2025 |
| 7 | Speedrun: Creating Your First Data Connection | Apr 24, 2025 |
| 8 | Model training in Jupyter Code Workspaces | Apr 25, 2025 |
| 9 | Tutorial: Supervised Machine Learning | Apr 27, 2025 |
| 10 | Final Challenge Tasks | Apr 28, 2025 |

---

## Featured: Bike Trips Data Pipeline

The core hands-on project was building a full data cleaning pipeline for a **bike-sharing dataset** using Foundry's Python Transforms.

### What it does
- Casts `StartTime` and `EndTime` columns to proper datetime types
- Filters out rows with null or empty `StartStation` / `EndStation` values
- Selects and outputs only the required columns: `TripID`, `StartStation`, `EndStation`, `StartTime`, `EndTime`
- Outputs a clean `BikeTrips_Processed` dataset (311 rows, 5 columns)

### Transform code

```python
from transforms.api import transform_pandas, Input, Output
import pandas as pd

@transform_pandas(
    Output("BikeTrips_Processed"),
    bike_trips=Input("bike_sharing_trips_clean")
)
def bike_trips_clean(bike_trips):
    # Cast timestamps
    bike_trips['StartTime'] = pd.to_datetime(bike_trips['StartTime'])
    bike_trips['EndTime'] = pd.to_datetime(bike_trips['EndTime'])

    # Filter invalid records
    processed_df = bike_trips[
        (~bike_trips['EndTime'].isnull()) & (bike_trips['EndTime'] >= bike_trips['StartTime'])
    ]

    # Filter to keep only rows where both StartStation and EndStation are not null or empty
    filtered_df = processed_df[
        (~processed_df['StartStation'].isnull()) & (processed_df['StartStation'].str.strip() != '') &
        (~processed_df['EndStation'].isnull()) & (processed_df['EndStation'].str.strip() != '')
    ]

    # Select required columns
    processed_df = filtered_df[['TripID', 'StartStation', 'EndStation', 'StartTime', 'EndTime']]

    return processed_df
```

### Build output

![Build success](screenshots/build_success.jpeg)
*Build completed successfully — 311 rows, 5 columns*

![Pipeline build progress](screenshots/build_progress.jpeg)
*Build progress: Starting → Spark → Running → Finished*

---

## Skills Practiced

- **Python Transforms** — `@transform_pandas`, Input/Output decorators, pandas data cleaning
- **Pipeline Builder** — no-code and code-based pipeline construction
- **Quiver & Contour** — in-platform data analysis and visualization
- **Jupyter Code Workspaces** — supervised ML model training
- **Foundry data connections** — registering and managing datasets
- **End-to-end workflows** — raw data → clean dataset → analysis → output

---

## Screenshots

| Module Overview | Build in Progress | Build Succeeded |
|---|---|---|
| ![modules](screenshots/modules_overview.jpeg) | ![progress](screenshots/build_progress.jpeg) | ![success](screenshots/build_success.jpeg) |

> Screenshots taken from Palantir Open Data Playground (opendataplayground.palantirfoundry.com)

---

## Context

- 🏆 Built as prep for **[Hack4Future Sicily 2025](https://hack4future.it/)** — reached Top 4 Finalist
- 📍 University of Messina, CS student (Minor: Data Science)
- 🔗 [LinkedIn](https://linkedin.com/in/nasywaarr)

---

*Palantir Foundry and Open Data Playground are products of Palantir Technologies. This repo contains only my own learning work and does not reproduce any proprietary platform content.*
