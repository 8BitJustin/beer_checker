from selenium import webdriver
import time

# driver = webdriver.Chrome()
# Delete below three lines and uncomment above driver line to show browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get("https://thetapandbottle.com/northstore")

print("Accessing website...\n")

time.sleep(5)

frame = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(frame)
driver.find_element_by_class_name('search-label').click()
driver.find_element_by_id("search").send_keys("left hand")

print('Searching...\n')

time.sleep(8)

print('Results...\n')

titles = driver.find_elements_by_css_selector('div.name.bold')

for title in titles:
	print(title.text)
