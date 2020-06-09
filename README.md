# Automated_Form_Fill_and_WebScraping
A project on getting essential details of a company's form filling process using webscraping and using Automated Form filling to fetch and pass on form data.

## Link to Web-scrape the data:
https://ebiz.licindia.in/D2CPM/#qni/basicinfo

## Task
Need to scrape and print insurance name (Jeevan Arogya), number of lives, policy term, age, and yearly premium.

## Approach
Since the data to be retrieved is Form-type, Selenium is used to automate the process.

## Libraries used
#### Web Scraping
> Selenium
> BeautifulSoup4
#### Initialise Chrome Driver
> ChromeDriverManager
#### Data Analysis
> Pandas
#### Other important libraries
> requess
> time

## How to run the File
Simply download the python file and run it either via cmd prompt or directly. Ensure all the dependencies have been installed. The script will take a while (approx. 30 sec) to initiate and establish connection with the chrome driver. Once the website is launced, forms will be filled automatically based on your inputs in the python file (modify details as per your needs). Do keep in mind a time delay of 10 sec is given before every POST to the next page to prevent presubmission of forms, and hence be patient!

