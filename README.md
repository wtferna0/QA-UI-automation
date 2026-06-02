# QA-UI-automation
# Safora QA Internship Assessment

## Part 2 - Basic UI Automation

### Framework Used

* Python
* Selenium WebDriver

### Automated Test Cases

#### 1. Contact Form Submission Test

This script:

* Opens the Safora Contact page
* Fills all required fields
* Clicks the Send Message button

File:

contact_form_positive_test.py


#### 2. Contact Form Validation Test

This script:

* Opens the Safora Contact page
* Leaves all fields empty
* Clicks the Send Message button
* Verifies that validation messages are displayed

File:

contact_form_validation_test.py

### Installation

Install Selenium:

pip install selenium


### Execution

Run Contact Form Submission Test:

python contact_form_positive_test.py

Run Validation Test:

python contact_form_validation_test.py


### Notes

The Safora Contact Us form uses Google reCAPTCHA protection. Therefore, complete end-to-end automated submission may require manual CAPTCHA verification. The automation focuses on form interaction, field validation, and submission workflow up to the CAPTCHA stage.
