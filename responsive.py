from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#! 리팩토링
class ResponsiveTester:
    def __init__(self,urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480,960,1366,1920]
        


    def screenshot(self,url):
        HEIGHT = self.browser.get_window_size()['height']
        self.browser.get(url)
        for width in self.sizes:
            self.browser.set_window_size(width,HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            print( scroll_size )
            total_sections = ceil(scroll_size/ HEIGHT)
            for section in range(total_sections + 1):
                self.browser.execute_script(f"window.scrollTo(0, {section * HEIGHT})")
                self.browser.save_screenshot(f"screenshots/{width}*{section+1}.png")
                time.sleep(2)


    def start(self):
        for url in self.urls:
            self.screenshot(url)

tester = ResponsiveTester(['https://google.com', "https://www.coupang.com"])
tester.start()

""" browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://nomadcoders.co/")
browser.maximize_window()

sizes= [480,960,1366,1920]

# print(browser.get_window_size())
HEIGHT = browser.get_window_size()['height']

for width in sizes:
    browser.set_window_size(width,HEIGHT)
    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    scroll_size = browser.execute_script("return document.body.scrollHeight")
    print( scroll_size )
    total_sections = ceil(scroll_size/ HEIGHT)
    for section in range(total_sections + 1):
        browser.execute_script(f"window.scrollTo(0, {section * HEIGHT})")
        browser.save_screenshot(f"screenshots/{width}*{section+1}.png")
        time.sleep(2)
 """