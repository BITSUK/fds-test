from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# driver.get("http://localhost:3000/")
driver.get("http://fdsapp.s3-website.ap-south-1.amazonaws.com")

title = driver.title
assert title == "FDS Web App"

driver.implicitly_wait(0.5)

print("=================================================")
print("== Functional Testing Starts (Selenium)        ==")
print("=================================================")
print("")

text_box = driver.find_element(by=By.NAME, value="search")
value = text_box.text
assert value == ""
print ('PASSED   Test 01: Check if website site is up.')
driver.implicitly_wait(1)

submit_button = driver.find_element(by=By.ID, value="srchBtn")

text_box.send_keys("Selenium")
print ('PASSED   Test 02: Able to interact.')
driver.implicitly_wait(3)

# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# value = message.text
# assert value == "Received!"
print ('SKIPPED  Test 02: Able to interact with backend.')
driver.implicitly_wait(2)

print("")
print("=================================================")
print("== Testing Ends                                ==")
print("=================================================")
print("")

driver.quit()