from selenium import webdriver
import time

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)


def search(*args):

	body = ''

	for arg in args:

		driver.get("https://thetapandbottle.com/northstore")

		print("\nAccessing website...\n")

		time.sleep(5)

		frame = driver.find_elements_by_tag_name('iframe')[0]

		driver.switch_to.frame(frame)
		driver.find_element_by_class_name('search-label').click()

		driver.find_element_by_id("search").send_keys(arg)

		print(f'\nSearching for requested brew... {arg.title()}\n')

		time.sleep(8)

		titles = driver.find_elements_by_css_selector('div.name.bold')
		prices = driver.find_elements_by_css_selector('span.price')

		print(f'\nLocated {len(titles)} items for {arg.title()}\n')

		fulldesc = dict(zip(titles, prices))

		body += f"You searched for: {arg.title()}\n\n"

		for t, p in fulldesc.items():
			body += '\t' + t.text + ' / $' + p.text + '\n\n'

	return body

