import requests
from bs4 import BeautifulSoup
import logging
import time
import os
import pandas as pd


os.makedirs("../data/raw", exist_ok=True)
os.makedirs("../data/log", exist_ok=True)

logging.basicConfig(filename="../data/log/scraper.log", level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")


csv_file = "../data/raw/jobs.csv"





def get_job_data(card):
    try:
        skills = []
        title = card.find('h2').find("a").get_text(strip=True)
        location = card.find('span', {'class': 'css-16x61xq'}).get_text()
        company = card.find('a', {'class': 'css-ipsyv7'}).get_text(strip=True)
        job_type = card.find('span', {'class': 'css-uofntu eoyjyou0'}).get_text()
        a = card.find_all('a', {'class': 'css-o171kl'})
        exp_level = a[1].text.strip() if len(a) > 0 else "N/A"
        duration = card.find('span', {'class': 'css-uc9rga eoyjyou0'}).get_text()
        date_posted = card.find("div", class_=["css-eg55jf", "css-1jldrig"]).get_text(strip=True)
        for skill in card.find_all('a', {'class': 'css-5x9pm1'}):
            skills.append(skill.get_text(strip=True).lstrip("· ").strip())
        skills = ", ".join(skills)
        salary = "Confidential"
        return {
            'title': title,
            'company': company,
            'location': location,
            'skills': skills,
            'Type': job_type,
            'Duration': duration,
            'experience_level': exp_level,
            'salary': salary,
            'date_posted': date_posted
        }
    except Exception as e:
        logging.error(f"Error parsing job card: {e}")
        return None


def run_scraper():
    if os.path.exists(csv_file):
        os.remove(csv_file)
    URL = 'https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt'
    for page in range(182):
        for attempt in range(5):
            try:
                jobs = []
                r =requests.get(URL, params={'start': page, 'ref': 'browse-jobs'}, timeout=15)
                r.raise_for_status()
                if "Please enable JavaScript" in r.text:
                    raise RuntimeError("Blocked by Cloudflare")
                soup = BeautifulSoup(r.text, 'html.parser')
                job_cards = soup.find_all("div", { "class" : "css-ghe2tq e1v1l3u10" })
                for card in job_cards:
                    data = get_job_data(card)
                    if data:
                        jobs.append(data)
                if jobs:
                    df = pd.DataFrame(jobs)
                    df.to_csv(
                        csv_file,
                        mode="a", 
                        index=False,
                        header=not os.path.exists(csv_file)
                        )
                print(f"Page {page} saved successfully.")
                logging.info(f"Page {page} saved ({len(jobs)} jobs)")
                time.sleep(2)
                break
            except Exception as e:
                wait_time = 5 * (2 ** attempt)
                logging.warning(f"Error on page {page}, attempt {attempt}: {e}")
                time.sleep(wait_time)
        else:
            logging.error(f"Skipping page {page} after 5 failed attempts.")



def main():
    try:
        run_scraper()
    except Exception as e:
        logging.error(f"Scraper stopped: {e}. Switching to fallback.")
        if os.path.exists('KAGGLE_FALLBACK'):
            print("Loading Kaggle fallback dataset...")
            df_fallback = pd.read_csv('KAGGLE_FALLBACK')
            df_fallback.to_csv(csv_file, index=False)
            logging.info("Successfully loaded Kaggle fallback data.")
        else:
            logging.critical("Fallback file not found!")


if __name__ == "__main__":
    main()
