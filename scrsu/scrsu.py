from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import datetime
import sys

t = datetime.datetime.now()

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://abc123") #mod abc123
    driver.find_element(By.XPATH, "//*[contains(text(), 'abc123')]").click() #mod abc123
except:
    print("err") #strona nie wchodzi
    exit()

time.sleep(10)

try:
    driver.find_element(By.XPATH, "//*[contains(text(), 'abc123')]") #mod abc123
except:
    pass
else:
    print("prv")
    exit()

try:
    driver.find_element(By.XPATH, "//*[contains(text(), 'abc123')]") #mod abc123
except:
    pass
else:
    print("off")
    exit()

try:
    driver.get_screenshot_as_file(t.strftime("%Y-%m-%d_%H-%M.png"))
except:
    pass
else:
    print("img")
    exit()

# instrukcja instalacji

# cat /etc/debian_version
# 12.4

# sudo apt-get update
# sudo apt-get install chromium chromium-driver
# sudo apt-get install python3-pip (nie wiem czy potrzeba)
# sudo apt install python3-selenium
