import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

data = [
    ['Patient 1', '2023-10-17 08:10:00', 1, 'Mild Chest Pain', 'Initial assessment'],
    ['Patient 1', '2023-10-17 09:00:00', 2, 'Worsening Chest Pain', 'Lack of response to treatment'],
    ['Patient 1', '2023-10-17 10:30:00', 3, 'Shortness of Breath', 'Delayed intervention'],
    ['Patient 1', '2023-10-17 12:00:00', 5.5, 'Heart Attack', 'Escalation to critical condition'],
    ['Patient 1', '2023-10-17 13:45:00', 3, 'Stabilized after Medication', 'Partial recovery'],

    ['Patient 2', '2023-10-17 08:20:00', 1, 'Headache', 'Initial complaint'],
    ['Patient 2', '2023-10-17 09:40:00', 3, 'Severe Headache and Dizziness', 'Escalation due to dehydration'],
    ['Patient 2', '2023-10-17 11:10:00', 2, 'Reduced Symptoms', 'Treated with IV fluids'],
    ['Patient 2', '2023-10-17 12:30:00', 1, 'Normal Condition', 'Full recovery'],

    ['Patient 3', '2023-10-17 08:50:00', 1, 'Nausea', 'Initial observation'],
    ['Patient 3', '2023-10-17 10:00:00', 2, 'Vomiting', 'Escalation due to infection'],
    ['Patient 3', '2023-10-17 11:30:00', 3, 'Dehydration', 'Requires immediate IV'],
    ['Patient 3', '2023-10-17 13:00:00', 4, 'Fever and Weakness', 'Escalation to high priority'],

    ['Patient 4', '2023-10-17 09:15:00', 2, 'Back Pain', 'Moderate discomfort'],
    ['Patient 4', '2023-10-17 10:45:00', 3, 'Increased Pain', 'Escalation due to lack of response'],
    ['Patient 4', '2023-10-17 12:15:00', 2, 'Pain Reduced', 'Responding to treatment'],

    ['Patient 5', '2023-10-17 08:05:00', 1, 'Cough and Sore Throat', 'Mild symptoms'],
    ['Patient 5', '2023-10-17 09:30:00', 2, 'High Fever', 'Escalation due to worsening condition'],
    ['Patient 5', '2023-10-17 11:00:00', 3.5, 'Shortness of Breath', 'Suspected respiratory issue'],
    ['Patient 5', '2023-10-17 12:45:00', 1, 'Recovered', 'Symptoms resolved']
]


# Load the data into a DataFrame
columns = ['Patient', 'Time', 'Severity', 'Issue', 'Escalation']
df = pd.DataFrame(data, columns=columns)

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each patient's events as individual lines
for patient in df['Patient'].unique():
    patient_data = df[df['Patient'] == patient]
    ax.plot(patient_data['Time'], patient_data['Severity'], marker='o', label=patient)

    # Add vertical lines and labels at the bottom
    for idx, row in patient_data.iterrows():
        # Add a vertical line from the data point to the x-axis
        ax.vlines(row['Time'], ymin=0, ymax=row['Severity'], color='gray', linestyle='dashed', alpha=0.5)

        # Add text label below the x-axis
        ax.text(
            row['Time'], -0.5,  # Slightly below the x-axis
            # f"{row['Issue']}\n({row['Escalation']})",
            f"{row['Issue']}",
            ha='center', va='top', rotation=90, fontsize=8
        )

# Highlight area above severity 3
ax.axhspan(3, 5, color='red', alpha=0.1)

# Format the x-axis to improve readability
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.xaxis.set_major_locator(mdates.HourLocator())

# Set labels and title
ax.set(title="Patient Severity over Time", ylabel="Severity", xlabel="Time")
plt.xticks(rotation=45)
ax.legend(title="Patients", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to avoid label clipping
plt.tight_layout()

# Show the plot
plt.show()
plt.pause(0.1)

### Bar Chart: Maximum Severity Reached ###
# Get the highest severity reached by each patient
max_severity = df.groupby('Patient')['Severity'].max()

# Create a bar plot
fig, ax_bar = plt.subplots(figsize=(8, 5))
max_severity.value_counts().sort_index().plot(kind='bar', ax=ax_bar, color='skyblue')

# Set labels and title
ax_bar.set(title="Number of Patients by Maximum Severity Reached",
           xlabel="Severity", ylabel="Number of Patients")

# Adjust layout and show the bar chart
plt.tight_layout()
plt.show()
plt.pause(0.1)
