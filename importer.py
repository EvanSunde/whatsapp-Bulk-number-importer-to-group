from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get('https://web.whatsapp.com/')

print("the script will run after 60 second.")
time.sleep(60)

# Open the file
with open('path_to_file', 'r') as file:
    lines = file.readlines()

# Type each line from the file into the active field
for line in lines:
    webdriver.ActionChains(driver).send_keys(line).perform()
    webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
    time.sleep(3)  

time.sleep(10)
driver.quit()
