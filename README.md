# Playwright project
The project implements parallel testing in several browsers at once
(you can also specify which one to use in tests). Also, at the end 
of the work, xml are created, html, tracing, Allure reports and screenshots. 
Allure reports are detailed, about each step.

## My stack
- Python
- Playwright
- Pytest

## Maintainer
- MasterAQA

## How to make an image in Docker
To build a Docker image, run the following commands:
```
git clone https://github.com/MasterAQA/playwright-framework.git
docker build -t playwright-test-framework . # it may take 500+ seconds
docker run -d -it playwright-test-framework 

Docker -> containers -> touch View files in new container
go to directory usr/src/ and edit file .env, put this environments in
APPLE_USERNAME = "fernardmiller443@gmail.com"
APPLE_PASSWORD = "SDA51345sadwq!"
```

## How to run
```
pytest tests/
# in docker run only in headless mode
# in docker make sure you are in the /usr/src/app directory
command for this: cd /usr/src/app
```

### By default, what pytest.ini uses:
Can change pytest.ini to run tests with your own settings, for example 
with one or two browsers, how many cores to burn tests and what reports 
to generate

Launch of 3 browsers: chromium, firefox, webkit
``` 
--browser chromium --browser firefox --browser webkit
``` 

Parallel running of tests
``` 
-n 3
``` 

Creation of xml, html, Allure reports
``` 
--junitxml=reports/report.xml
--alluredir reports/allure_report/
--html=reports/html_report/report.html
``` 

## Test cases that were used to test this site
- test_login_page - check authorization with successful data and 
wait for a 2-factor authentication request on the screen
- test_main - check the main categories of the site and access 
to search from home page 
- test_search_page - check the search function
- test_store_page - check the function of add an item to 
the cart, and in another test add to the cart with remove the 
item from the cart, check that the cart is empty

## Website URL used for testing
- https://www.apple.com









