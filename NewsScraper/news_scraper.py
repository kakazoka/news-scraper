import csv
from datetime import datetime
import logging
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def configure_webdriver():
    service = Service(SERVICE_PATH)

    options = Options()
    options.add_argument('--headless')
    return webdriver.Edge(service=service, options=options)


def scrape_articles(driver):
    logging.info('Opening Metacritic Games web page.')
    driver.get('https://www.metacritic.com/game/')

    logging.info('Localizing articles.')
    articles = driver.find_elements(By.CLASS_NAME, 'c-articleSummary')

    logging.info('Scraping articles.')
    latest_articles = []
    for article in articles:
        try:
            title = article.find_element(By.CLASS_NAME, "c-articleSummary_title").text.strip()
            description = article.find_element(By.CLASS_NAME, "c-articleSummary_description").text.strip()
            link = article.find_element(By.CLASS_NAME, 'c-articleSummary_container').get_attribute('href')

            if title and description:
                latest_articles.append({'Title': title, 'Description': description, 'Link': link})
        except Exception as error:
            logging.warning(f'Error scraping an article: {error}.')

    logging.info('Articles scraped. Closing Metacritic Games web page.')
    driver.quit()
    return latest_articles


def save_articles(news):
    save_path = Path(SAVE_PATH)
    save_path.mkdir(parents=True, exist_ok=True)

    current_date = datetime.now().strftime('%d-%m-%Y')

    csv_path = save_path / f'news_{current_date}.csv'

    if news:
        logging.info(f'Saving articles to {csv_path}.')
        with csv_path.open('w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Description', 'Link'])
            writer.writeheader()
            writer.writerows(news)
    else:
        logging.warning('No articles found. The .csv file was not created.')
