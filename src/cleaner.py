import pandas as pd
import os

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

def split_location(loc):
    loc = str(loc)
    if loc.count(',') == 2:
        city, governorate, country = loc.split(',')
    elif loc.count(',') == 1:
        city, country = loc.split(',')
        governorate  = city
    else:
        city = loc
        governorate = "unknown"
        country = "unknown"
    return city, governorate, country

df[['city', 'governorate', 'country']] = df['location'].apply(
    lambda x: pd.Series(split_location(x))
)
df.drop(columns=['location'], inplace=True)


df.to_csv('../output/jobs_cleaned.csv', index=False)
print(f"Done! Cleaned {len(df)} jobs and saved to ../output/jobs_cleaned.csv")
