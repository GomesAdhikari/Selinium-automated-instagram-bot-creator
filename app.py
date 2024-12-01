from script.instagram_signup import (
    create_driver, sign_up, captcha_solve, date_selection, confirm_otp, save_to_csv
)
from script.temprory_mail import get_temp_email, get_otp
from script.name_username import generate_random_name, generate_username
from script.proxy_handler import load_proxies, get_proxy_detail
from script.logger import logger
from script.customexception import CustomException
from threading import Thread
import time
import sys
if __name__ == "__main__":
    try:
        # Step 1: Load proxies and start periodic proxy update
        #logger.info("Loading proxies...")
        #proxy_list = load_proxies('proxies_list.txt')  # Corrected function call to load proxies

        #if not proxy_list:
           # logger.error("No proxies loaded. Exiting.")
          #  exit()
        # Initial proxy selection
        #logger.info("Selecting initial proxy...")
        for i in range(10):
            username,password,ip,port = ("toIc-sessTime-1",'gautam','11.5.102','33')
            ip_port = ip + ':' + port
            if not ip:
                logger.error("No valid proxies available. Exiting.")
                exit()

        # Step 2: Driver Initialization
            print('selected_proxy =',i)
            logger.info("Initializing driver with selected proxy...")
            driver, tabs = create_driver(username=username,password=password,endpoint=ip,port=port,selected_proxy=ip)

        # Step 3: Fetch Temporary Email
            logger.info("Fetching temporary email...")
            temp_mail = get_temp_email(driver)

        # Switch back to the main tab after fetching the email
            driver.switch_to.window(tabs[0])

        # Step 4: Generate Random Name and Username
            logger.info("Generating random name and username...")
            first, last, fullname = generate_random_name()
            username_1 = generate_username(first=first, last=last)
            password = 'Gautam1@'  # Consider using secure storage for passwords

        # Step 5: Sign Up Process
            logger.info("Starting signup process...")
            driver = sign_up(driver, temp_mail, username_1=username_1, name=fullname)

        # Step 6: Date of Birth Selection
            logger.info("Selecting date of birth...")
            driver = date_selection(driver)

        # Step 7: Captcha Solving
            #logger.info("Solving captcha...")
            #driver = captcha_solve(driver)

        # Step 8: Get OTP from Temporary Email
            logger.info("Fetching OTP...")
            driver.switch_to.window(tabs[1])  # Switch to the temp email tab
            otp = get_otp(driver)

        # Step 9: Confirm OTP
            logger.info("Confirming OTP...")
            driver.switch_to.window(tabs[0])  # Switch back to the main tab
            driver = confirm_otp(driver, number=otp)

        # Step 10: Save Account Details to CSV
            logger.info("Saving account details to CSV...")
            save_to_csv(driver=driver, username_1=username_1)
            logger.info("Signup process completed successfully.")

    except Exception as e:
            raise CustomException(e,sys)
            logger.error(f"An error occurred: {e}")
    finally:
            # Ensure the driver is properly closed if it exists
        if 'driver' in locals() and driver:
            driver.quit()
            logger.info("Driver closed.")
