import pandas as pd
import os
from collections import Counter
import ast
from itertools import combinations

if not os.path.exists('../output/jobs_cleaned.csv'):
    print("No raw data found to clean!")
    exit()

df = pd.read_csv('../output/jobs_cleaned.csv')

def top_hiring_companies():
    sorted_companies = df['company'].value_counts()
    return sorted_companies

def most_demanded_skills(n=10): # Add n=10 here
    actual_lists = df['skills'].dropna().apply(ast.literal_eval)
    frequency = Counter(x for lst in actual_lists for x in lst)
    return dict(frequency.most_common(n))

def average_experience_by_role():
    avg_exp = df.groupby('title')['experience_level_int'].mean().sort_values(ascending=False)
    return avg_exp


def skill_correlation_matrix():
    actual_lists = df['skills'].dropna().apply(ast.literal_eval)
    pair_counter = Counter()

    for skills in actual_lists:
        sorted_skills = sorted(skills)
        pairs = combinations(sorted_skills, 2)
        pair_counter.update(pairs)

    top_pairs = pair_counter.most_common(20)
    matrix_df = pd.DataFrame([
        {'Skill 1': pair[0], 'Skill 2': pair[1], 'Times Appeared Together': count}
        for pair, count in top_pairs
    ])
    return matrix_df