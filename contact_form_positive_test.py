# contact_form_positive_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

try:
    # Open Contact Page
    driver.get("https://safora.se/en/contact.html")
    driver.maximize_window()

    # Fill Contact Form
    driver.find_element(By.ID, "name").send_keys("Nathasha Fernando")
    time.sleep(1)


    driver.find_element(By.ID, "email").send_keys(
        "nathasha.testing@gmail.com"
    )
    time.sleep(1)


    driver.find_element(By.ID, "phone").send_keys(
        "0771234567"
    )
    time.sleep(1)


    driver.find_element(By.ID, "message").send_keys(
        "This is a Selenium automation test for the Safora Contact Us form."
    )
    time.sleep(1)


    # Click Send Message button
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    # Wait to observe result
    time.sleep(5)

    print("Form submission process executed successfully.")

except Exception as e:
    print("Test Failed:")
    print(e)

finally:
    driver.quit()
