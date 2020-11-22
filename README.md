# Beer Checker

Simple program that, when ran, displays results from local business of desired
 beer searched for.

## About

I love Left Hand Brewery, they are definitely my go-to when I need a good
 drink. So, to simplify the process of going to a website, confirming my age
 , searching
 , and seeing what the local Tap and Bottle has, I made a simple script that
  accesses the website that shows their inventory, searches for a premade
   key word, which then prints the results.
   
   Initial commit is the basic form of the build, v1.0. From here, I will be
    adjusting it to email me daily with Tap and Bottle's Left Hand Brewery
     inventory so I know in advance what to grab from there.
### Getting Started/Prerequisites

What is needed for this to work.

Python 3 (3.7 used)

Selenium (webdriver)


### Installing

Download or clone the repo.

Place into desired folder.

Ensure Python is installed.

Install Selenium
```
pip install selenium
```

## Running Script

If using PyCharm, within the project directory, simply run the main.py file.

If using the terminal, while in the project directory, type the following:
```
python main.py
```

To change the search parameter, change the parameter within the send_keys
 method.
```
driver.find_element_by_id("search").send_keys("INPUT SEARCH HERE")
```

## Versions

- V2.0
  - 11/22/2020
  - Program simplified. As send_email.py didn't need to be used multiple
   times, the code for it was reworked and placed within oktane.py, along
    with main.py code. Program now works out of one file, as send_email.py
     is no longer used.
- v1.0
  - 11/15/2020
  - Initial commit. Both main.py and send_email.py both used, main.py input
   within launchPy.bat file

## Built With

-   [Python](https://www.python.org/) - Programming Language Used
-   [Selenium](https://pypi.org/project/selenium/) - Automates Web Browser Interaction

## Authors

-   **Justin Olson** - _Initial work_ - [Portfolio](https://jodportfolio.herokuapp.com/)

## Acknowledgments

-   Kaden
-   Stack Overflow
-   Google Searching
