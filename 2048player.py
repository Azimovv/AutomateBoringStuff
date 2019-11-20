from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

def run2048():
    for i in range(100):
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

tryAgain = browser.find_element_by_class_name('retry-button')
while True:
    run2048()
    if tryAgain:
        tryAgain.click()
        run2048()
    else:
        break

