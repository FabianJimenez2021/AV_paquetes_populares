from selenium import webdriver 

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.get("https://github.com")
browser.find_element()