$readmeContent = @"

# 🇪🇬 Egypt Tech Job Market Analyzer

A full-stack data engineering pipeline that scrapes, cleans, and analyzes the IT job market in Egypt using Wuzzuf data. This project provides a deep dive into the local tech landscape, identifying the most in-demand skills, top-hiring companies, and geographic hubs.

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Scraping:** BeautifulSoup4, Requests
- **Data Processing:** Pandas, NumPy
- **Analysis:** Matplotlib, Seaborn
- **API:** Flask (REST API)

## 📊 Key Data Insights

### 1. The "Engineering" Benchmark

Technical roles are not just about coding; **"Engineering"** is the top requirement with nearly **800 mentions** in the dataset. This indicates a strong market preference for candidates with formal engineering backgrounds.

### 2. Geographic Monopoly

The analysis reveals a massive centralization of the tech economy:

- **Cairo:** ~68% of all jobs.
- **Giza:** ~20% of all jobs.
- Combined, the **Greater Cairo Area accounts for over 80%** of the IT market.

### 3. Soft Skills vs. Technical Skills

While technical skills like SQL and JavaScript are common, **"Communication"** ranks as the 3rd most demanded skill overall, appearing in over **600+ postings**.

## 📁 Project Structure

- `Scraper.py`: Crawls Wuzzuf and handles pagination/retries.
- `cleaner.py`: Performs feature engineering on locations and experience levels.
- `analyzer.py`: Generates statistics and skill correlation matrices.
- `visualizer.py`: Creates data visualizations (Bar, Pie charts).
- `api.py`: A Flask REST API to serve data as JSON.
- `notebooks/eda.ipynb`: Interactive data exploration.

## 💻 How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
