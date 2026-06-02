# contact_form_validation_test.py


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

try:
    driver.get("https://safora.se/en/contact.html")
    driver.maximize_window()

    # Submit form without entering any data
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    # Get HTML5 validation message from Name field
    name_field = driver.find_element(By.ID, "name")

    validation_message = driver.execute_script(
        "return arguments[0].validationMessage;",
        name_field
    )

    print("Validation Message:")
    print(validation_message)

    assert validation_message != ""

    print("Validation Test Passed")

    time.sleep(10)

except Exception as e:
    print("Test Failed:")
    print(e)

finally:
    driver.quit()
