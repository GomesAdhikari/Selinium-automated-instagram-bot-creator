from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time
import sys
from script.customexception import CustomException
def get_temp_email(driver):
    driver.get('https://temp-mail.io/en')
    
    try:
        # Allow the page to load and wait for the email element
        time.sleep(3)
        email_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        )
        return email_element.get_attribute('value') # Return the email address
    except Exception as e:
        print("Could not fetch email from Temp-Mail:", e)
        return None
    
def get_otp(driver):
    try:
        try:
            refresh = driver.find_element(By.XPATH,"//button[@data-qa='refresh-button']")
            refresh.click()
            consent_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'fc-button') and contains(@class, 'fc-primary-button')]"))
            )
            consent_button.click()
            print("Consent button clicked.")
        except Exception :
            print("No 'Consent' button found. Proceeding to fetch email.")
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-qa="message-subject"]'))
        )

    # Extract the inner text from the element
        inner_text = element.get_attribute('innerHTML')
        
    # Use regex to find all digits in the text
        match = re.search(r'\d+', inner_text)

        if match:
            number = match.group()
            print(f"Extracted number: {number}")
        else:
            print("No number found.")
        return number
    except Exception as e:
        raise CustomException(e,sys)
    