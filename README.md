# HHA507 Data Science Assignment
## Module 2: Healthcare Data Exploration with SQLite and Pandas

This task involves selecting a publicly available healthcare dataset, loading it into a local SQLite database, and performing various SQL queries to analyze the data. By utilizing the power of SQLite and pandas, this allowed me to explore and practice by selecting, counting, grouping, and sorting the available dataset of my choice.

My Chosen Healthcare Dataset: [Mental Health Data](/Users/raqsmacbookair/python/sqlite_dataexploration/mental_health_data.csv)

*Note:* Synthetic Data ⇧

# My Journey Through Python Using Visual Studio Code: STEPS, ERRORS, and TROUBLESHOOTING

1. I searched for and downloaded a public healthcare dataset from `Kaggle.com`.
    - 📌 I encountered several issues using Visual Studio Code (VSC) due to the attachment of the CSV file. However, with the help of my classmate Danny, I was able to solve the issue. I will focus on what gave me the most frustration. I was doing my practice assignment first before submitting my formal assignment to GitHub. When I was ready to submit after creating a repository and following the steps I had taken previously, I got stuck at `pip install -r requirements.txt` I reached out to my classmate and my professor. Before I read my professor’s response, I entered the `pip install pandas` command in VSC under the 'requirements.txt' file, and it was successful! A simple step and command that I missed, which I will definitely never miss again. After this successful step, I proceeded to set up my chosen database and queries as instructed in this assignment.

2. Setting Up a Local SQLite Database
    - 📌 I used pandas to load my dataset into the SQLite database.
        - I keep getting errors due to the values of my data. However, I found that I missed entering some values for some of the chosen data/columns.

3. Performing SQL Queries to Explore and Analyze the Data
    - (1) Selected all records based on specific “Symptoms.”
    - (2) Filtered records based on “Symptoms” having “Trouble Sleeping” by “Gender (Male)."
    - (3) Grouped records by “Diagnosis/Condition” and calculated the average “Age.”
    - (4) Sorted records by “Duration (weeks)” to show the top 5 records with the highest duration.

# My Key Takeaways from this Assignment

### - 📌 Problem-solving, Humility, and Collaboration
- By asking for help from my classmate and professor when I encountered issues in this assignment, I believe it demonstrated my problem-solving skills.
- Recognizing that I need assistance and being open to learning from others are key aspects of staying humble and grounded.
- Collaborating with others can be crucial in overcoming technical skills, particularly for a beginner like me.

### - 📌 Attention to Detail
- The importance of paying attention to small details such as the correct commands for the installation packages `pip install pandas`, can prevent significant roadblocks.

### - 📌 Data Handling and Analysis
- I was able to practice loading data into a database and performing several `SQL` queries, which are fundamental skills in data analysis. I still find it difficult, but like what professor said "Practice makes perfect."

### - 📌 Learning from My Mistakes
- Encountering and resolving errors is a critical part of my learning process. Each mistake provides a learning opportunity for me that can improve my future assignments and work.
