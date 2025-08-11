import pandas as pd
import numpy as np 
from datetime import datetime, timedelta
# You have a DataFrame containing user session data from the Roblox platform. 
# Each row represents a session with the following columns: user_id, session_id, start_time, end_time, experience_id, device_type. 
# Calculate the average session duration for each experience, broken down by device type.

# Expected Output:
# A DataFrame showing the average session duration in minutes for each experience and device type combination.

# Generate sample data
np.random.seed(42)
user_ids = np.random.randint(1000, 9999, 1000)
session_ids = np.random.randint(10000, 99999, 1000)
start_times = [datetime(2023, 1, 1) + timedelta(hours=np.random.randint(0, 720)) for _ in range(1000)]

# Fix: Convert numpy.int64 to Python int
durations = [int(x) for x in np.random.randint(5, 180, 1000)]  # Session durations in minutes
end_times = [start + timedelta(minutes=duration) for start, duration in zip(start_times, durations)]
experience_ids = np.random.choice(['game_A', 'game_B', 'game_C', 'game_D', 'game_E'], 1000)
device_types = np.random.choice(['mobile', 'tablet', 'desktop', 'console'], 1000)

# Create DataFrame
session_data = pd.DataFrame({
    'user_id': user_ids,
    'session_id': session_ids,
    'start_time': start_times,
    'end_time': end_times,
    'experience_id': experience_ids,
    'device_type': device_types
})

# Calculate session duration in minutes
session_data['duration_minutes'] = (session_data['end_time'] - session_data['start_time']).dt.total_seconds() / 60

# Group by experience_id and device_type to get average session duration
avg_duration = session_data.groupby(['experience_id', 'device_type'])['duration_minutes'].mean().reset_index()

# Format the result
avg_duration['duration_minutes'] = avg_duration['duration_minutes'].round(2)

print(avg_duration)