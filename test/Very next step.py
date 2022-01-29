from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


def input_data():
    namefield = browser.find_element_by_name("firstname").send_keys("Jeyhun")
    lastname = browser.find_element_by_name("lastname").send_keys("Tester")
    email = browser.find_element_by_name("email").send_keys("test@mail.ru")

def file_upload():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "testfile.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_data()
    file_upload()
    submit = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()