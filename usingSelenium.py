from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('*******@gmail.com')
next = browser.find_element_by_id('identifierNext')
next.click()
passwordElem = browser.find_element_by_id('password')
passwordElem.click()
passwordElem = browser.find_element_by_class_name('whsOnd.zHQkBf')
passwordElem.send_keys('********')
next = browser.find_element_by_id('passwordNext')
next.click()