# 510_lab4
### Overview
A world clock app and schedule for hello.py and scraper.py in Github action.
### How to run
- Installation :```pip install -r requirements.txt```
- Usage :```streamlit run app.py```
- I put the code for scraping website into scraper.py and scheduled it every day
- I scheduled hello.py every 30 mins using action
### Lessons learned
- Learned how to set manual trigger for workflow
- Learned how to add UNIX timestamp display to a Streamlit application and created a separate page for converting UNIX timestamps to human-readable time.
- Learned how to create and configure a GitHub Actions workflow to perform web crawling tasks at regular intervals, including setting up workflow files and scheduling times.
### Questions/Future improvements
- Still didn’t succeed in inserting Data into a PostgreSQL Database on Azure

