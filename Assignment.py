#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def load_timecard(file_path):
    """ This function loads the timecard data from the Excel file given."""
    
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)
    
    # Assuming that the 'Time' and 'Time Out' columns are in datetime format
    df['Time'] = pd.to_datetime(df['Time'])
    df['Time Out'] = pd.to_datetime(df['Time Out'])
    
    # Sort the DataFrame by employee name and time to facilitate analysis
    df.sort_values(by=['Employee Name', 'Time'], inplace=True)
    
    return df

def calculate_consecutive_days(prev_time, current_time):
    """ Calculate if the current time is part of a consecutive workday."""
    # Check if the current row is part of a consecutive workday
    if prev_time is None or (current_time - prev_time).days == 1:
        return True
    return False

def analyze_timecard_row(prev_time, current_time, current_employee, current_position):
    """
    Analyze a row of the timecard and print relevant information.

    Parameters:
    - prev_time (pd.Timestamp or None): Previous time.
    - current_time (pd.Timestamp): Current time.
    - current_employee (str): Employee name.
    - current_position (str): Employee position.
    """
    # Check if the current row is part of a consecutive workday
    if calculate_consecutive_days(prev_time, current_time):
        print(f"{current_employee} ({current_position}) has worked for 7 consecutive days.")
    
    time_between_shifts = (current_time - prev_time).seconds / 3600 if prev_time else 0
    if 1 < time_between_shifts < 10:
        print(f"{current_employee} ({current_position}) has less than 10 hours between shifts but more than 1 hour.")
    
    shift_duration = (current_time - current_time).seconds / 3600 if prev_time else 0
    if shift_duration > 14:
        print(f"{current_employee} ({current_position}) has worked for more than 14 hours in a single shift")

def analyze_timecard(df):
    """
    Analyze the timecard and print relevant information.

    Parameters:
    - df (pd.DataFrame): Timecard data.
    """
    # Initialize variables for tracking consecutive days
    prev_time = None
    
    # Iterate through rows to analyze the timecard
    for _, row in df.iterrows():
        current_employee = row['Employee Name']
        current_position = row['Position ID']  # Adjust column name based on your data
        current_time = row['Time']
        
        analyze_timecard_row(prev_time, current_time, current_employee, current_position)
        
        # Update previous time
        prev_time = current_time

# File path
filename = r"C:\Users\hp\OneDrive\Desktop\MCA BVICAM\Assignment_Timecard.xlsx"

# Load timecard data
timecard_data = load_timecard(filename)

# Analyze the timecard
analyze_timecard(timecard_data)


# In[ ]:




