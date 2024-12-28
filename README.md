# News Scraper
This automation scrapes the latest game-related articles from the Metacritic website using Selenium, extracting the title, description and link to each article, and saves the data into a .csv file.

## Features
- Extracts article titles, descriptions and links from Metacritic's games page
- Saves the scraped data in a structured .csv file for easy access and analysis
- Operates in headless mode to ensure a seamless and non-intrusive experience
- Provides detailed logs for each step of the process, including warnings for any scraping errors

## Installation
1. Clone the repository:
```
git clone https://github.com/kakazoka/news-scraper.git
```
2. Install the required Python package:
```
pip install selenium
```
3. Download the WebDriver:
- [Google Chrome WebDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br)
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)
- [Mozilla Firefox WebDriver](https://github.com/mozilla/geckodriver)

## Usage
1. Set up paths:
- Define ```SERVICE_PATH``` to point to the WebDriver executable
- Define ```SAVE_PATH``` to specify the directory where the .csv files should be saved
2. Run the script:
```
python main.py
```
3. Output:
- The script will generate a .csv file in the specified SAVE_PATH
