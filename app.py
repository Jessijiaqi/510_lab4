import streamlit as st
import pytz
from datetime import datetime
import time

# List of time zones
time_zones = list(pytz.all_timezones)

# Use Streamlit's new feature for pages if available, or a simple sidebar selection otherwise
page = st.sidebar.selectbox('Choose a page', ['Clocks', 'UNIX Timestamp Converter'])

if page == 'Clocks':
    # Sidebar for selecting up to 4 locations
    selected_timezones = st.sidebar.multiselect('Select up to 4 locations', time_zones, default=["UTC"], max_selections=4)

    # Container to display clocks
    clocks_container = st.empty()

    while True:
        with clocks_container.container():
            # Display the current time for each selected location along with the UNIX timestamp
            for tz in selected_timezones:
                now = datetime.now(pytz.timezone(tz))
                unix_timestamp = int(time.mktime(now.timetuple()))
                st.metric(label=tz, value=f"{now.strftime('%Y-%m-%d %H:%M:%S')}\nUNIX: {unix_timestamp}")
        
        # Update every second
        time.sleep(1)
elif page == 'UNIX Timestamp Converter':
    st.title('UNIX Timestamp Converter')

    # User input for UNIX timestamp
    user_input = st.number_input('Enter UNIX timestamp', step=1)

    # Convert and display the human-readable time
    if user_input:
        human_time = datetime.utcfromtimestamp(user_input).strftime('%Y-%m-%d %H:%M:%S UTC')
        st.write('Human-readable time:', human_time)

