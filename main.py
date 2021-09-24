from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = 'buy domain'

browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://google.com")


#! elemnts가 아니라 element
search_bar = browser.find_element_by_class_name('gLFyf')

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name('g')


#! 검색 후 테스트 추출
# for search_result in search_results:
#     title = search_result.find_element_by_tag_name("h3")
#     if title:
#         print(title.text)

#! 스크린샷

#* 대기시켜서 동적인 요소 선택
useless_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"ULSxyf")))

# useless_element.screenshot('wow.png')

#* 자바스크립트 실행
browser.execute_script(
    
"""
const wrong = arguments[0];
wrong.parentElement.removeChild(wrong)

""",
useless_element
)

# print(useless_element)
for index, search_result in enumerate(search_results):
    # class_name = search_result.get_attribute('class')
    # print(class_name)
    # if 'jNVrwc Y4pkMc' and 'VjDLd mnr-c g-blk' not in class_name:
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png") 

#! 종료
browser.quit()