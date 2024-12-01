from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from script.customexception import CustomException
import time
import pandas as pd
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re
import sys
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from script.logger import logger
from script.extension import proxies

def create_driver(username,password,endpoint,port,selected_proxy):
    api_key = 'your api key'
    extension_path = r"E:\Captcha Solver Auto Recognition and Bypass - Chrome Web Store 3.7.2.0.crx"
    chrome_options = Options()
    #chrome_options.add_extension(extension_path)
    proxies_extension = proxies(username, password, endpoint, port)
    chrome_options.add_extension(proxies_extension)
    logger.info('extention integration started')
    if selected_proxy:
        logger.info(f'Proxy {selected_proxy} added to the driver')
    else:
        logger.critical('Running without proxy')
    
    driver = webdriver.Chrome(options=chrome_options)
    #driver.get("chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html")  # Replace <extension-id> with actual ID

# Toggle the first switch
    #toggle_switch_1 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='autoSubmitForms' and @id='autoSubmitForms']")
    #toggle_switch_1.click()

# Toggle the second switch
    #toggle_switch_2 = driver.find_element(By.XPATH, "//div[@class='switch']/input[@name='autoSolveRecaptchaV2']")
    #toggle_switch_2.click()

# Enter API key
    #api_key_input = driver.find_element(By.NAME, "apiKey")
    #api_key_input.send_keys(api_key)
    
# Locate and click the login button
    #login_button = driver.find_element(By.ID, "connect")
    #login_button.click()
    #logger.info('Added extension successfully')
  #  try:
        # Handle any alert that appears after clicking the login button
      #  alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
      #  alert.accept()
      #  logger.info("Alert accepted.")
  #  except TimeoutException:
   #     logger.info('No alert Present moving to sign up')
    driver.get('https://www.instagram.com/')
    driver.execute_script("window.open('');")
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.get('https://temp-mail.io/en')
    logger.info('returned driver and tabs from (create_driver) function succesfully')
    return driver,tabs

def sign_up(driver,temp_email,username_1,name):

    try:
        
        allow_cookies_button = driver.find_element(By.XPATH, "//button[contains(@class, '_a9--') and contains(@class, '_ap36') and contains(@class, '_a9_0')]")
        
        allow_cookies_button.click()
        print("Allow all cookies button clicked.")
    except Exception:
        print("No 'Allow all cookies' button found. Proceeding to sign up.")

    try:
        time.sleep(2)
        # Wait for and click the "Sign up" button
        sign_up_button = driver.find_element(
                By.XPATH, "//span[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacw') and contains(@class, '_aad0') and contains(@class, '_aad7')]"
        )
        
        sign_up_button.click()
        print("Sign up button clicked.")
    except Exception as e:
        print("Could not click sign-up button on Instagram:", e)
        return

    
    try:
        email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "emailOrPhone"))
)
        email_field.send_keys(temp_email)

        password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
)
        password.send_keys('Gautam1@')
        full_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "fullName"))
)
        full_name.send_keys(name)
  # Adjust time as needed for waiting

        username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Username"]'))
) 
        username.send_keys(username_1)
        sign_up_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Next" or text()="Sign up"]'))
    )
        sign_up_button.click()
        logger.info('returned driver and tabs from (signup) function succesfully')
        return driver
    except Exception as e:
        raise CustomException(e,sys)

def date_selection(driver):
    month_element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//select[@title="Month:"]'))
    )
    day_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@title="Day:"]'))
    )
    year_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@title="Year:"]'))
    )
    # Create Select objects for interacting with the dropdowns
    month_select = Select(month_element)
    day_select = Select(day_element)
    year_select = Select(year_element)

# Generate a random date
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 28)  # Safe choice for all months
    random_year = random.randint(1970, 2004)

# Select the random values from the dropdowns
    month_select.select_by_value(str(random_month))
    day_select.select_by_value(str(random_day))
    year_select.select_by_value(str(random_year))

# Optional: Print the selected date
    print(f"Selected Date: {random_month}/{random_day}/{random_year}")
    next_button = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "_acan") and contains(@class, "_acap") and contains(@class, "_acaq") and contains(@class, "_acas") and contains(@class, "_aj1-") and contains(@class, "_ap30")]'))
    )
    next_button.click()
    print("Next button clicked.")
    time.sleep(5)

    
    return driver
def captcha_solve(driver):
    try:
        next_button = driver.find_element(By.XPATH,"//button[contains(@class,'_acan')]")
        next_button.click()
    except:
        pass
    return driver


def confirm_otp(driver,number):
    try:
        input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email_confirmation_code"))
    )
    
    # Input the confirmation code into the field
        input_field.send_keys(number)
        print("Code entered successfully.")
    except Exception as e:
        print("Failed to find or interact with the confirmation code input field:", e)

    next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Next')]"))
)
    next_button.click()
    return driver
def save_to_csv(driver,username_1,csv_filename='accounts.csv'):
    try:

        # Wait for the SVG element with the aria-label="Instagram" to appear
        #WebDriverWait(driver, 20).until(
          #  EC.presence_of_element_located((By.XPATH, "//svg[@aria-label='Instagram']"))
       # )

        # If found, create a new entry and append to the CSV
        new_entry = {'Username': username_1, 'Password': 'Gautam1@'}

        # Check if the file 
        # sts
        if os.path.exists(csv_filename):
            # Read the existing CSV and append the new entry
            df = pd.read_csv(csv_filename)
            df = df.append(new_entry, ignore_index=True)
        else:
            # Create a new DataFrame if the file does not exist
            df = pd.DataFrame([new_entry], columns=['Username', 'Password'])

        # Save the DataFrame to CSV without overwriting the existing file
        df.to_csv(csv_filename, index=False)
        print("Data appended to CSV file.")
    except Exception as e:
        print("Error during Instagram form fill or saving:", e)

    