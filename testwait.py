from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 100)
    driver.get("http://google.com")  
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("Irwin Kwan")
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='irwinhkwan.com']")))
    site = driver.find_element_by_xpath("//a[@href='irwinhkwan.com']")
    site.click()
    
    driver.quit()