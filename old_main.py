# Legacy code, no longer used. Stored for archive purposes

from selenium import webdriver
import time
import send_email

print('Running...')

# driver = webdriver.Chrome()
# Delete below three lines and uncomment above driver line to show browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

# Website being accessed
driver.get("https://thetapandbottle.com/northstore")

print("Accessing website...")

time.sleep(5)

# Accessing frame with needed data
frame = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(frame)
# Search box isn't visible by default, the 'Search' button needs to be
# clicked for it to show
driver.find_element_by_class_name('search-label').click()

# Text being added to search box
# To change the search item, change the parameter within send_keys
driver.find_element_by_id("search").send_keys("left hand")

print('Searching...')

time.sleep(8)

# Takes all of the elements that are <div> with .name and .bold, stores in list
titles = driver.find_elements_by_css_selector('div.name.bold')

print('Sending email...\n')
# Sends email of beer list to desired email
send_email.sending(titles)

print('Email sent!')

print('Closing!')

# Closes python box after program finishes
driver.close()
driver.quit()