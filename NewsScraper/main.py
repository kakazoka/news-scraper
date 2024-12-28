from news_scraper import configure_webdriver, scrape_articles, save_articles


if __name__ == '__main__':
    driver = configure_webdriver()
    news = scrape_articles(driver)
    save_articles(news)
