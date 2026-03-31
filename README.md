# 🛠️ Palantir Foundry — Learning & Prep

> Pre-hackathon preparation for **Hack4Future Sicily 2025**
> Platform: [Palantir AIP / Open Data Playground](https://www.palantir.com/platforms/foundry/)

---

## About

This repository documents my hands-on preparation with **Palantir Foundry** ahead of Hack4Future Sicily 2025 — an inter-university hackathon across Sicily focused on data-driven innovation.

Over ~4 weeks, I worked through 11 structured learning modules on the Open Data Playground, earned 7 Palantir certifications, and built multiple real pipelines covering data cleaning, feature engineering, REST API integration, and workflow debugging.

---

## Certifications

| Certificate | Completed |
|---|---|
| Introduction to Foundry & AIP for Enterprise Organizations | Feb 21, 2025 |
| Scoping Use Cases for Foundry & AIP | Feb 21, 2025 |
| Foundry & AIP Builder Foundations Quiz | Feb 22, 2025 |
| Deep Dive: Building Your First Pipeline | Mar 31, 2025 |
| Deep Dive: Creating Your First Data Connection | Apr 2, 2025 |
| Deep Dive: Data Analysis in Contour | Apr 16, 2025 |
| Deep Dive: Data Analysis in Quiver | Apr 17, 2025 |

---

## Modules Completed

| # | Module | Last Updated |
|---|--------|-------------|
| 1 | Speedrun: Your First E2E Workflow | Mar 31, 2025 |
| 2 | Deep Dive: Building your first Pipeline | Mar 31, 2025 |
| 3 | No-code approach to data cleaning with Pipeline Builder | Apr 2, 2025 |
| 4 | Deep Dive: Data Connection | Apr 2, 2025 |
| 5 | Deep Dive: Data Analysis in Quiver | Apr 17, 2025 |
| 6 | Parse different data formats in Pipeline Builder | Apr 18, 2025 |
| 7 | Deep Dive: Data Analysis with Contour | Apr 23, 2025 |
| 8 | Speedrun: Creating Your First Data Connection | Apr 24, 2025 |
| 9 | Model training in Jupyter Code Workspaces | Apr 25, 2025 |
| 10 | Tutorial: Supervised Machine Learning | Apr 27, 2025 |
| 11 | Final Challenge Tasks | Apr 28, 2025 |

---

## Final Challenge Tasks

### Challenge 1: Build an End-to-End Workflow
Built a complete pipeline from raw bike-sharing data through to a processed output dataset, combining Pipeline Builder and Python Transforms.

Datasets: `all_data`, `bike_sharing_trips`, `BikeTrips_Pipeline`, `Python Transform`

### Challenge 3: Workflow Debugging and Optimization
Built and debugged a garbage collection route optimization workflow involving geospatial scheduling data.

Datasets: `bin_locations`, `collection_schedule`, `Daily_Collection_Route`, `Daily_Waste_Collection_Schedule_python`, `garbage_collection_pipeline`, `Route Output`

---

## Featured: Bike Trips Data Pipeline

The core hands-on project was building a full data cleaning and feature engineering pipeline for a **bike-sharing dataset** using Foundry's Python Transforms.

### bike_trips_clean.py — Data Cleaning
- Casts `StartTime` and `EndTime` columns to proper datetime types
- Filters out rows with null or empty `StartStation` / `EndStation` values
- Selects and outputs only the required columns: `TripID`, `StartStation`, `EndStation`, `StartTime`, `EndTime`
- Outputs a clean `BikeTrips_Processed` dataset (311 rows, 5 columns)

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

### trip_transforms.py — Feature Engineering
- Calculates trip duration in minutes
- Extracts day of week and hour of day from start time
- Filters out trips with zero or negative duration

```python
import pandas as pd

def transform(inputs):
    df = inputs["all_data"]

    # Convert to datetime
    df["StartTime"] = pd.to_datetime(df["StartTime"])
    df["EndTime"] = pd.to_datetime(df["EndTime"])

    # Calculate trip duration in minutes
    df["Duration_Minutes"] = (df["EndTime"] - df["StartTime"]).dt.total_seconds() / 60

    # Extract day of week and hour
    df["DayOfWeek"] = df["StartTime"].dt.day_name()
    df["HourOfDay"] = df["StartTime"].dt.hour

    # Remove trips with negative or zero duration
    df = df[df['Duration_Minutes'] > 0]

    return {
        "transform_bike_trips": df
    }
```

### Build output

![Build success](screenshots/build_success.jpeg)
*Build completed successfully — 311 rows, 5 columns*

![Pipeline build progress](screenshots/build_progress.jpeg)
*Build progress: Starting → Spark → Running → Finished*

---

## Skills Practiced

- **Python Transforms** — `@transform_pandas`, Input/Output decorators, data cleaning and feature engineering
- **Pipeline Builder** — no-code filter transforms, graph-based pipeline construction, Python transform nodes
- **Quiver & Contour** — in-platform data analysis and visualization
- **Jupyter Code Workspaces** — supervised ML model training
- **Foundry data connections** — registering and managing datasets, REST API calls
- **Ontology Manager** — exploring object types, link types, and action types
- **Workshop** — building ontology-backed UI modules with pie chart widgets and object filters
- **End-to-end workflows** — raw data → clean dataset → feature engineering → analysis → output

---

## Screenshots

| Module Overview | Build in Progress | Build Succeeded |
|---|---|---|
| ![modules](screenshots/modules_overview.jpeg) | ![progress](screenshots/build_progress.jpeg) | ![success](screenshots/build_success.jpeg) |

> Screenshots taken from Palantir Open Data Playground (opendataplayground.palantirfoundry.com)

---

## Context

- 🏆 Built as prep for **[Hack4Future Sicily 2025]** — reached Top 4 Finalist
- 📍 University of Messina, CS student (Minor: Data Science)
- 🔗 [LinkedIn](https://linkedin.com/in/nasywaarr)

---

*Palantir Foundry and Open Data Playground are products of Palantir Technologies. This repo contains only my own learning work and does not reproduce any proprietary platform content.*
