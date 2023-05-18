from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
from selenium_stealth import stealth
stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32",
        webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True,)
from selenium.common.exceptions import NoSuchElementException

total_list = []
driver.implicitly_wait(5)

link = "https://vk.com/nugabest.russia"
driver.get(link)
for post in range(1, 11):

    button_xpath = '//div[' + str(post) + ']//span[text()="Show more"]'
    post_xpath = '//div[' + str(post) + ']//div[@class="wall_post_text"]'
    try:
        button = driver.find_element(By.XPATH, button_xpath)
        driver.execute_script("return arguments[0].click();", button)
        time.sleep(2)
        post_element = driver.find_element(By.XPATH, post_xpath)
        post_text = post_element.text
        total_list.append(post_text)

    except NoSuchElementException:
        print(f"In post {post} text is not present")
        continue

for n, item in enumerate(total_list, start=1):
    print(f'{n})  {item} ')
    print()

driver.quit()
