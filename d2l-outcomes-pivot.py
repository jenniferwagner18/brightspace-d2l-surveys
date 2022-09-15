# Pivots text data from CSV file generated from mastery view of learning outcomes ETL data flow 
# Data flow is at https://github.com/jenniferwagner18/brightspace-etl-dataflows/blob/main/mastery-view.md
# Output matches Mastery View table in D2L with students in rows, outcomes in columns, and levels as values

import pandas as pd
import numpy as np

df = pd.read_csv('outcomes.csv')
df = df.iloc[:, [1,2,3,4]] # columns to pivot (2nd column is first name, 3rd is last name, etc. in my 
df.columns = ['FirstName', 'LastName', 'Outcomes', 'Levels']
table = pd.pivot_table(df, values='Levels', index=['FirstName', 'LastName'], columns='Outcomes', aggfunc=lambda x: ' '.join(x))
table.to_csv('mastery-view.csv')
