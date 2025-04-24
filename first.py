from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qa-practice.netlify.app/bugs-form.html")

# expected_title = "QA Practice | Learn with RV"
# actual_title = driver.title

# if expected_title == actual_title:
#     print("Test is Succesful")
# else:
#     print("Test is Failed",actual_title)

button = driver.find_element(By.ID,"registerBtn")
# click on the button
button.click()
# locate the error element
message_element = driver.find_element(By.ID,"message")
# get innerHTML from error element
actual_message = message_element.get_attribute("innerHTML")
expected_message = "The password should contain between [6,20] characters!"
# check if the text == expected_text
if expected_message == actual_message:
    print("Message Test case Sucessful ")
else: 
    print("Message Test case failed")

driver.quit()
