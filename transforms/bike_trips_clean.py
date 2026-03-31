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
