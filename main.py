from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# specify the path to chromedriver
driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(driver_path)

# Open WhatsApp web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Update 'Friend's Name' to the actual name of your friend or a group
target_name = '"Friend\'s Name"'

# Update the message you want to send
message_text = "Hello from Python!"

target_xpath = '//span[contains(@title,' + target_name + ')]'
target_title = wait.until(EC.presence_of_element_located((By.XPATH, target_xpath)))
target_title.click()

input_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_elements_by_xpath(input_xpath)[0]

# Send the message
input_box.send_keys(message_text + Keys.ENTER)

# Wait to see the result
time.sleep(2)

# Close the driver
driver.quit()
