# Selenium Scraper for Submitted Cases

This Python script utilizes Selenium to scrape information about submitted cases from a specific website. The script is designed to work with the Chrome browser and requires the ChromeDriver executable.

## Prerequisites

Before running the script, ensure that you have the following:

1. [Chrome browser](https://www.google.com/chrome/)
2. [ChromeDriver](https://sites.google.com/chromium.org/driver/) - Download and place the executable in the specified location (`C:\\Program Files\\chromedriver.exe`).

## Installation

Clone the repository:

```bash
git clone <repository-url>
Install the required Python packages:

bash
Copy code
pip install selenium pandas
Usage
Set the path to the ChromeDriver executable in the webdriver.Chrome() function.
Run the script:
bash
Copy code
python script_name.py
```
Replace script_name.py with the actual name of your Python script.

The script will open the specified URL and start scraping information about submitted cases.
The scraped data will be displayed in the console, including details about each case.
Important Note
The script is designed to handle pagination. It identifies the last row with the text "page {page_counter}" as an indication to move to the next page.
Adjust the waiting times and conditions based on the specific characteristics of the website and your requirements.
It is recommended to run the script responsibly and be aware of the website's terms of service.
Feel free to customize and extend the script according to your scraping needs. Happy scraping!