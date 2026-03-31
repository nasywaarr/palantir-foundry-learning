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

    # Return the output
    return {
        "transform_bike_trips": df
    }
