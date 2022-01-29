from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    trollface = browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    open_new_window = browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    entertext = browser.find_element_by_id("answer").send_keys(result)
    submit = browser.find_element_by_tag_name("button").click()



finally:
    time.sleep(5)
    browser.quit()
