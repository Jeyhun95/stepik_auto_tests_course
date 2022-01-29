from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    buttonclick = browser.find_element_by_tag_name("button").click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    entertext = browser.find_element_by_id("answer").send_keys(result)
    submit = browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
