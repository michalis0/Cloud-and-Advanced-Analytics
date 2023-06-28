"""An example of showing geographic data."""

import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="NYC Ridesharing Demo", page_icon=":taxi:")


# LOAD DATA ONCE
@st.cache_resource
def load_data():
    path = "uber-raw-data-sep14.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/{path}"

    data = pd.read_csv(
        path,
        nrows=100_000,  # approx. 10% of data
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )
    return data


# FILTER DATA FOR A SPECIFIC HOUR, CACHE
@st.cache_data
def filterdata(df, hour_selected):
    """
    This function filters a Pandas DataFrame containing Uber ridesharing data, selecting only the rows where the hour of
    the pickup matches the specified hour. It uses Streamlit's caching feature to cache the filtered DataFrame, so it
    only needs to be computed once. It returns the resulting filtered DataFrame.
    """
    # YOUR CODE HERE
    return ...


# STEP 1: LOAD DATA AND FILTER BY HOUR
# Complete the code to perform the following based on the previous functions:
# YOUR CODE HERE
#   1. Load the data into a dataframe.
data = ...
#   2. Create a slider to filter the data by the hour.
hour = ...
#   3. Filter the data by the hour.
data = ...
#   4. Display the data in a table.
...


# Now go to streamlit/uber_example_step_02.py to continue.
# In this file we will add a histogram to the sidebar and a map to the main area as well as maps for the main airports of NYC.
# The squeleton of the code is already there, you just need to fill in the blanks.
# The solution will be released after the lab