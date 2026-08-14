# Egypt Tech Job Market: Data Engineering & Analytics Pipeline

A robust, end-to-end data pipeline designed to monitor and analyze the Software Development job market in Egypt. This project implements web scraping, data cleaning, statistical analysis, and a RESTful API to deliver actionable market intelligence.

## 🏗️ System Architecture

The project is structured as a modular ETL pipeline:

1.  **Extraction Layer:** Automated web scraping of the Wuzzuf job portal.
2.  **Transformation Layer:** Cleaning, normalization, and feature engineering of unstructured job data.
3.  **Analytical Layer:** Statistical processing and visualization of market trends.
4.  **Service Layer:** A Flask-based REST API for data consumption.

---

## 🛠️ Technical Implementation

### 1. Data Acquisition (Scraper)

- **Engine:** Built using `BeautifulSoup4` and `Requests`.
- **Resiliency:** Implements an exponential backoff retry strategy to handle network instability and rate limiting.
- **Logging:** Centralized logging system tracks scraping progress and records failed attempts in `data/log/scraper.log`.
- **Validation:** Includes a runtime check for Cloudflare/JavaScript challenges and a fallback mechanism to local datasets.

### 2. Data Engineering (ETL)

- **Normalization:** Standardizes job titles, company names, and skill tags into lowercase, stripped formats.
- **Feature Engineering:**
  - **Geospatial Processing:** Splits raw location strings into distinct 'City', 'Governorate', and 'Country' features.
  - **Ordinal Encoding:** Maps categorical experience levels (e.g., 'Entry Level', 'Manager') to an integer-based 'Experience Index' for correlation analysis.
- **Deduplication:** Removes redundant entries to maintain data integrity.

### 3. Analytics & Visualization

- **Skill Correlation:** Computes co-occurrence matrices to identify common technology clusters.
- **Geographical Analysis:** Quantifies market concentration across governorates.
- **Visualization:** Utilizes `Seaborn` and `Matplotlib` to generate production-ready insights in `.png` format.

---

## 📈 Market Insights (Key Findings)

- **Geographical Concentration:** Analysis shows that **92.2% of IT vacancies** are concentrated within the Greater Cairo Area (Cairo & Giza).
- **Skill Demand Distribution:** **"Engineering"** is the most frequent requirement (**~800 occurrences**), indicating a market prioritized toward architectural and systems roles over entry-level coding.
- **Professional Requirements:** **Communication Skills** rank among the top three requirements, appearing in over **75% of senior-level postings**.

---

## 🔌 API Documentation

The project includes a Flask-based REST API for programmatic access to the analytics:

| Endpoint              | Method | Description                                                              |
| :-------------------- | :----- | :----------------------------------------------------------------------- |
| `/skills/top`         | GET    | Returns the Top N most demanded skills in JSON format.                   |
| `/companies/top`      | GET    | Returns a ranked list of companies with the highest hiring volume.       |
| `/skills/correlation` | GET    | Returns a matrix of skill pairings that appear together in job postings. |

---

## 🚀 Installation & Execution

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/YouanesAttia/egypt-tech-job-analyzer.git
    cd egypt-tech-job-analyzer
    ```

2.  **Environment Setup:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Pipeline:**

    ```bash
    python src/Scraper.py
    python src/cleaner.py
    ```

4.  **Launch API Service:**
    ```bash
    python api.py
    ```

---

**Author:** [Youanes Attia](https://github.com/YouanesAttia)  
**License:** MIT
