from analyzer import top_hiring_companies, most_demanded_skills, average_experience_by_role, skill_correlation_matrix, df
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_top_skills():
    top_skills = most_demanded_skills().most_common(20)
    skills, counts = zip(*top_skills)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=list(counts), y=list(skills), palette="viridis")
    plt.title('Top 20 Most Demanded Tech Skills in Egypt', fontsize=16, pad=15)
    plt.xlabel('Number of Job Postings', fontsize=12)
    plt.ylabel('Skill', fontsize=12)
    plt.tight_layout()
    
    plt.savefig('../output/top_20_skills.png', dpi=300)
    plt.show()

def plot_top_companies():
    sorted_companies = top_hiring_companies()
    sorted_20_companies = sorted_companies.iloc[1: 21]
    plt.figure(figsize=(12, 8))
    sns.barplot(x=sorted_20_companies.values, y=sorted_20_companies.index, palette="viridis")
    plt.title('Top 20 Most Hiring Companies in Egypt', fontsize=16, pad=15)
    plt.xlabel('Number of Job Postings', fontsize=12)
    plt.ylabel('Company', fontsize=12)
    plt.tight_layout()    
    plt.savefig('../output/top_20_companies.png', dpi=300)
    plt.show()

def plot_experience_by_role():
    avg_exp = average_experience_by_role()
    top_20_exp = avg_exp.dropna().head(20)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_20_exp.values, y=top_20_exp.index, palette="mako")
    plt.title('Top 20 Roles Requiring the Highest Average Experience', fontsize=16, pad=15)
    plt.xlabel('Average Experience Level', fontsize=12)
    plt.ylabel('Job Title', fontsize=12)
    plt.tight_layout()
    plt.savefig('../output/average_exp_by_role.png', dpi=300)
    plt.show()

