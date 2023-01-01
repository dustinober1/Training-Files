import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/Users/dustinober/Downloads/chromedriver")

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(executable_path="/Users/dustinober/Downloads/chromedriver")
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  """Extract only the temp from the text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(3)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(3)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(3)
  print(driver.current_url)

print(main())