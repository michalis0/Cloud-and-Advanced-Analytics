
"""An example of showing geographic data."""
import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="NYC Ridesharing Demo", page_icon=":taxi:")


# ==========================================================================================================
# ==========================================================================================================
# ================================== FIRST WE DEFINE SOME HELPER FUNCTIONS =================================
# ==========================================================================================================
# ==========================================================================================================
# LOAD DATA ONCE
@st.cache_resource
def load_data():
    """
    This function loads data from a CSV file containing Uber ridesharing data. It reads the file into a Pandas DataFrame,
    setting column names and parsing the date/time column as datetime. The function uses Streamlit's caching feature to
    load the data only once, and it returns the resulting DataFrame.
    """
    path = "uber-raw-data-sep14.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/{path}"

    data = pd.read_csv(
        path,
        nrows=100000,  # approx. 10% of data
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
    return df[df["date/time"].dt.hour == hour_selected]


# CALCULATE MIDPOINT FOR GIVEN SET OF DATA
@st.cache_data
def mpoint(lat, lon):
    """
    This function calculates the midpoint of a set of latitude and longitude coordinates, using the numpy.average()
    function. It uses Streamlit's caching feature to cache the result, so it only needs to be computed once. It returns
    a tuple containing the latitude and longitude of the midpoint.
    """
    return (np.average(lat), np.average(lon))


# FILTER DATA BY HOUR
@st.cache_data
def histdata(df, hr):
    """
    Filter the given DataFrame to include only rows where the hour
    of the "date/time" column is greater than or equal to the given
    hour and less than the next hour, then calculate a histogram of
    the minutes within that hour and return a Pandas DataFrame with
    the minute and pickup count for each minute.
    """
    filtered = data[ (df["date/time"].dt.hour >= hr) & (df["date/time"].dt.hour < (hr + 1))]
    hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0, 60))[0]
    return pd.DataFrame({"minute": range(60), "pickups": hist})


# ==========================================================================================================
# ==========================================================================================================
# ==================================== THEN WE "DESIGN" THE WEB APP PAGE ===================================
# ==========================================================================================================
# ==========================================================================================================
# STREAMLIT APP LAYOUT
data = load_data()

# LAYING OUT THE TOP SECTION OF THE APP WITH 2 COLUMNS
row1_1, row1_2 = st.columns((2, 3)) # Size of columns 2, 3 means 2/5 and 3/5 of the screen

with row1_1:
    st.title("NYC Uber Ridesharing Data") # Title of the app
    hour_selected = st.slider("Select hour of pickup", 0, 23) # Slider to select hour of pickup


with row1_2:
    # Just a text to explain the app
    st.write(
        """
    ##
    Examining how Uber pickups vary over time in New York City's and at its major regional airports.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """
    )

# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1)) # Size of columns 2, 1, 1, 1 

# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
la_guardia = [40.7900, -73.8700] # Latitude and longitude of La Guardia Airport
jfk = [40.6650, -73.7821] # Latitude and longitude of JFK Airport
newark = [40.7090, -74.1805] # Latitude and longitude of Newark Airport
zoom_level = 12 # the map will be zoomed in to show the airport in detail
midpoint = mpoint(data["lat"], data["lon"]) # the map will be centered on the midpoint of all the data points


# FUNCTION FOR AIRPORT MAPS
def map(data, lat, lon, zoom):
    """
    This function creates a PyDeck map with a hexagonal heatmap layer, based on the input data and the specified
    latitude, longitude, and zoom level. It returns the resulting PyDeck map as a Streamlit component.
    ----
    :param data: a pandas dataframe containing the data to be visualized on the map
    :param lat: the latitude coordinate of the map center
    :param lon: the longitude coordinate of the map center
    :param zoom: the initial zoom level of the map
    ----
    :return: a PyDeck map as a Streamlit component
    """
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )

# DISPLAYING THE MAPS
# The maps are displayed in the middle section of the app, with the NYC map on the left and the airport maps on the right
# The maps are displayed using the map() function defined above
with row2_1:
    st.write(
        f"""**All New York City from {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
    )
    map(filterdata(data, hour_selected), midpoint[0], midpoint[1], 11)

with row2_2:
    st.write("**La Guardia Airport**")
    map(filterdata(data, hour_selected), la_guardia[0], la_guardia[1], zoom_level)

with row2_3:
    st.write("**JFK Airport**")
    map(filterdata(data, hour_selected), jfk[0], jfk[1], zoom_level)

with row2_4:
    st.write("**Newark Airport**")
    map(filterdata(data, hour_selected), newark[0], newark[1], zoom_level)


# CALCULATING DATA FOR THE HISTOGRAM
chart_data = histdata(data, hour_selected)

# LAYING OUT THE HISTOGRAM SECTION
st.write(f"""**Breakdown of rides per minute between {hour_selected}:00 and {(hour_selected + 1) % 24}:00**""")

st.altair_chart(
    alt.Chart(chart_data)
    .mark_area(
        interpolate="step-after",
    )
    .encode(
        x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
        y=alt.Y("pickups:Q"),
        tooltip=["minute", "pickups"],
    )
    .configure_mark(opacity=0.2, color="red"),
    use_container_width=True,
)