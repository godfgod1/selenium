from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://google.com")

#! elemnts가 아니라 eLement
search_bar = browser.find_element_by_class_name('gLFyf')

search_bar.send_keys('hello!')

browser.quit()