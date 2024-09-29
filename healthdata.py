import pandas as pd
import sqlite3


### 1) I searched and downloaded a Public Healthcare Dataset. I utilized dataset from Kaggle.com. *Note: synthetic data was used*

df = pd.read_csv('mental_health_data.csv')


### 2) Setting up a local SQLite Database
conn = sqlite3.connect('mentalhealth.db')

df.to_sql('health_data', conn, if_exists='replace', index=False)

### Created Pandas to load my dataset into the SQLite database. 
healthdata = {
    'User ID': [1, 2, 3, 4, 15, 26],
    'Age': [56, 69, 46, 32, 57, 50],
    'Gender': ['Non-binary', 'Non-binary', 'Non-binary', 'Other','Female', 'Male'],
    'Symptoms': ['feeling anxious', 'trouble sleeping', 'feeling irritable', 'feeling sad', 'feeling anxious', 'loss of interest in activities'],
    'Duration (weeks)': ['21', '42', '26', '44', '49', '7'],
    'Therapy History': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes'],
    'Diagnosis / Condition': ['Depression', 'Panic Disorder', 'Stress', 'Anxiety', 'Anxiety', 'Burnout'],
    'Suggested Therapy': ['Cognitive Behavioral Therapy', 'No therapy needed', 'Cognitive Behavioral Therapy', 'Support Groups', 'No therapy needed', 'Psychotherapy'],
    'Self-care Advice': ['Exercise', 'Take Breaks', 'Take Breaks', 'Journaling', 'Journaling', 'Meditation'],
}
df = pd.DataFrame(healthdata)


print(df.head())

df.shape
len(df)
df.columns
df.dtypes
df.describe()

df ['Diagnosis / Condition']. value_counts ( )
df ['Symptoms']. value_counts ( )
df ['Self-care Advice']. value_counts ( )
df ['Suggested Therapy']. value_counts ( )
df ['Age']. value_counts ( )



symptoms = df[df['Diagnosis / Condition'] == 'symptoms']
symptoms.head()

age = df[df['Diagnosis / Condition'] == 'age']
age.head()

duration = df[df['Diagnosis / Condition'] == 'duration']
duration.head()



### 3) I performed SQL queries to explore and analyze the data in my chosen SQLite database.

# (1) Selecting all records based on specific "Symptoms."

healthquery1 = "SELECT * FROM health_data WHERE Symptoms IN ('feeling sad', 'feeling irritable')"

result_df = pd.read_sql(healthquery1, conn)

print(result_df)

conn.close()


# (2) Based on Symptoms-Having "Trouble Sleeping" BY "Gender (Male)."

healthquery2 = "SELECT * FROM health_data WHERE Gender = 'Male' AND Symptoms = 'trouble sleeping'"

result_df = pd.read_sql(healthquery2, conn)

print(result_df)

conn.close()


# (3) Grouped by "Diagnosis / Condition" and calculated the average "Age".

healthquery3 = "SELECT `Diagnosis / Condition`, AVG(Age) as avg_age FROM health_data GROUP BY `Diagnosis / Condition`"

result_df = pd.read_sql(healthquery3, conn)

print(result_df)

conn.close()


# (4) Sorted by "Duration (weeks)"" which shows the top 10 records with the highest duration.

healthquery4 = "SELECT * FROM health_data ORDER BY `Duration (weeks)` DESC LIMIT 10"

result_df = pd.read_sql(healthquery4, conn)

print(result_df)

conn.close()

