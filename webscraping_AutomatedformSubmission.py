# import libraries

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time


# Initialise Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ebiz.licindia.in/D2CPM/#qni/basicinfo")
# Implicitly delaying to allow data to load after automated form filling
driver.implicitly_wait(20)


# Automate Form Filling

# Page 1
text_input = driver.find_element_by_id("da_textfieldupper-1084-inputEl")
text_input.send_keys("DONALD")
text_input = driver.find_element_by_id("da_textfieldupper-1085-inputEl")
text_input.send_keys("JOHN")
text_input = driver.find_element_by_id("da_textfieldupper-1088-inputEl")
text_input.send_keys("TRUMP")
text_input = driver.find_element_by_id("da_datefield-1090-inputEl")
text_input.send_keys("15/01/1999")
text_input = driver.find_element_by_id("da_textfield-1102-inputEl")
text_input.send_keys("donaldtrump@gmail.com")
text_input = driver.find_element_by_id("da_numberfield-1099-inputEl")
text_input.send_keys("9000090000")
maleRadioBtn = driver.find_element_by_id("radio-1095-inputEl")
maleRadioBtn.click()
search_button = driver.find_element_by_id("da_button-1107-btnInnerEl")
search_button.click()

time.sleep(10)
text_input = driver.find_element_by_id("da_button-1110-btnIconEl")
text_input.click()




# Page 2, 3
checkboxElement = driver.find_element_by_class_name("x-grid-checkcolumn")
checkboxElement.click()
search_button = driver.find_element_by_id("da_button-1140-btnInnerEl")
search_button.click()



# Page 4
radio_input = driver.find_element_by_id("radio-1158-inputEl")
radio_input.click()
radio_input = driver.find_element_by_id("radio-1161-inputEl")
radio_input.click()
radio_input = driver.find_element_by_id("da_radiofield-1163-inputEl")
radio_input.click()
text_input = driver.find_element_by_id("da_combo-1172-inputEl")
text_input.send_keys("59")
text_input = driver.find_element_by_id("da_combo-1174-inputEl")
text_input.send_keys("3000")

search_button = driver.find_element_by_id("da_button-1185-btnInnerEl")
search_button.click()



content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# Initialising Lists to store data
insurance_name=[]
number_of_lives=[]
premium_type=[]
policy_term=[]
age=[]
yearly_premium=[]



# Retrieving values
time.sleep(5)
i_name = driver.find_element_by_id("da_label-1197").text
no_of_l = driver.find_element_by_id("da_label-1203").text
p_type = driver.find_element_by_id("da_label-1211").text
p_term = driver.find_element_by_id("da_label-1218").text
a = driver.find_element_by_id("da_label-1228").text
y_premium = driver.find_element_by_id("da_label-1281").text



# Printing Retrieved Values
print(i_name)
print(no_of_l)
print(p_type)
print(p_term)
print(a)
print(y_premium)



# Appending data to Lists
insurance_name.append(i_name)
number_of_lives.append(no_of_l)
premium_type.append(p_type)
policy_term.append(p_term)
age.append(a)
yearly_premium.append(y_premium)



# Writing data to CSV
df = pd.DataFrame({'Insurance name':insurance_name,'Number of Lives':number_of_lives, 'Premium type':premium_type, 'Policy Term':policy_term, 'Age':age, 'Yearly Premium':yearly_premium}) 
df.to_csv('C:/Users/DELL/Desktop/summer/Internship/FinalInsurance.csv', index=False, encoding='utf-8')

