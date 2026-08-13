import pandas as pd
import os
import numpy as np

if not os.path.exists('../data/raw/jobs.csv'):
    print("No raw data found to clean!")
    exit()

df = pd.read_csv('../data/raw/jobs.csv')

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['title'] = df['title'].str.lower().str.strip()
df['company'] = df['company'].str.lower().str.rstrip('  -').str.strip()
df['location'] = df['location'].str.lower().str.strip()
df['skills'] = df['skills'].str.lower().str.strip()
df['Type'] = df['Type'].str.lower().str.strip()
df['Duration'] = df['Duration'].str.lower().str.strip()
df['experience_level'] = df['experience_level'].str.lower().str.strip()
df['salary'] = df['salary'].replace('Confidential', None)

conditions = [
    df["experience_level"] == 'experienced',
    df["experience_level"] == 'manager',
    df["experience_level"] == 'entry level'
]
choices = [2, 3, 1]
df['experience_level_int'] = np.select(conditions, choices, default=np.nan)

def split_location(loc):
    loc = str(loc)
    parts = [p.strip() for p in loc.split(',')]
    if len(parts) == 3:
        city, governorate, country = parts
    elif len(parts) == 2:
        city, country = parts
        governorate = city
    else:
        city = parts[0]
        governorate = "unknown"
        country = "unknown"
    return city, governorate, country

df[['city', 'governorate', 'country']] = df['location'].apply(
    lambda x: pd.Series(split_location(x))
)
df.drop(columns=['location'], inplace=True)


df.to_csv('../output/jobs_cleaned.csv', index=False)
print(f"Done! Cleaned {len(df)} jobs and saved to ../output/jobs_cleaned.csv")
