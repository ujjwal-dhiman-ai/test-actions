import pytz
import csv
from datetime import datetime

# Get a list of all available time zones
time_zones = pytz.all_timezones

# Initialize a list to store time zone data
time_zone_data = []

# Get the current time for each time zone and add it to the list
for tz_name in time_zones:
    tz = pytz.timezone(tz_name)
    current_time = datetime.now(tz)
    time_zone_data.append([tz_name, current_time.strftime('%Y-%m-%d %H:%M:%S')])

# Define the CSV file name
csv_file_name = 'time_zones.csv'

# Write the time zone data to a CSV file
with open(csv_file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Time Zone', 'Current Time'])
    csv_writer.writerows(time_zone_data)

print(f'Time zone data saved to {csv_file_name}')
