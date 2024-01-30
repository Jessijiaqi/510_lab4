import streamlit as st
import pytz
from datetime import datetime
import time  # Import the time module

# List of time zones
time_zones = list(pytz.all_timezones)

# Sidebar for selecting up to 4 locations
selected_timezones = st.sidebar.multiselect('Select up to 4 locations', time_zones, default=["UTC"], max_selections=4)

# Container to display clocks
clocks_container = st.empty()

while True:
    with clocks_container.container():
        # Display the current time for each selected location
        for tz in selected_timezones:
            now = datetime.now(pytz.timezone(tz))
            st.metric(tz, now.strftime("%Y-%m-%d %H:%M:%S"))

    # Update every second
    time.sleep(1)
