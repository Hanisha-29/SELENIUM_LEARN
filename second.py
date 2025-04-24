from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

user_fn="Hanisha"
user_ln="Ladhipeerla"
user_pn=8561210916
user_cn="India"
user_email="abc@gmail.com"
user_pw="Hani$ha2"

def find_by_id(element):
    return driver.find_element(By.ID,element)

def get_innerhtml(element):
    return element.get_attribute("innerHTML")

def compare(expected,actual):
    if expected == actual:
        print("Pass")
    else:
        print("Fail",actual,expected)

driver=webdriver.Chrome()
driver.get("https://qa-practice.netlify.app/bugs-form.html")

# identify first name text field
first_name=find_by_id("firstName")
# set first name as Hanisha
first_name.send_keys(user_fn)
# pause the website for 5 mins ,giving time in seconds 
# time.sleep(300)

last_name=find_by_id("lastName")
last_name.send_keys(user_ln)

phone_number=find_by_id("phone")
phone_number.send_keys(user_pn)

# select value from dropdown 
country=Select(find_by_id("countries_dropdown_menu"))
country.select_by_visible_text(user_cn)

email_address=find_by_id("emailAddress")
email_address.send_keys(user_email)

password=find_by_id("password")
password.send_keys(user_pw)

check_box= find_by_id("exampleCheck1")
check_box.click()

button=find_by_id("registerBtn")
button.click()

# checking what is written in code is same as output 
result_fn=find_by_id("resultFn")
actual_first_name=get_innerhtml(result_fn)
expected_first_name="First Name: "+ user_fn
compare(expected_first_name,actual_first_name)

result_ln=find_by_id("resultLn")
actual_last_name=get_innerhtml(result_ln)
expected_last_name="Last Name: "+ user_ln
compare(expected_last_name, actual_last_name)

result_phone=find_by_id("resultPhone")
actual_phone=get_innerhtml(result_phone)
expected_phone="Phone Number: "+str(user_pn)
compare(expected_phone,actual_phone)

result_country=find_by_id("country")
actual_country=get_innerhtml(result_country)
expected_country="Country: "+ user_cn
compare(expected_country,actual_country)

result_email=find_by_id("resultEmail")
actual_email=get_innerhtml(result_email)
expected_email="Email: "+ user_email
compare(expected_email,actual_email)

time.sleep(100)

driver.quit()

