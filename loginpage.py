import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@given(u'open browser')
def open_browser(context):
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://hms-qa.recoup.health/login")


@when(u'provide valid "{username}" and "{password}"')
def login_page(context, username, password):
    try:
        context.driver.find_element(By.ID, "email").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys(password)
        button_element = context.driver.find_element(By.XPATH, '//*[@id="root"]//button')
        button_element.click()
    except Exception as e:
        print(f"Error during login: {e}")
        assert False, "Failed to log in"


@then(u'go to all patient')
def book_app(context):
    element = context.driver.find_element(By.XPATH, "//span[@class='ant-menu-title-content' and text()='All Patients']")
    element.click()
    time.sleep(3)
    input_sec = context.driver.find_element(By.ID, "customer_name")
    input_sec.send_keys("6382586867")
    input_sec.send_keys(Keys.ENTER)
    time.sleep(2)
    customer_xpath = "//table/tbody/tr[2]/td[1]"

    # Step 4: Wait for the element to be visible (with dynamic customer name)
    customer_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, customer_xpath)))
    customer_element.click()
    time.sleep(2)
    booking = context.driver.find_element(By.ID, "Schedule Appointment")
    booking.click()



@then(u'verify successful login or error message')
def verify_login(context):
    time.sleep(3)  # Give time for page to load
    try:
        # Check if login was successful by verifying the home page title
        if "Recoup Health Provider" in context.driver.title:
            print("Successfully logged in and verified home page title")
        else:
            # If login is not successful, check for an error message
            WebDriverWait(context.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Invalid username or password")]'))
            )
            print("Login failed: Invalid username or password error displayed.")
    except Exception as e:
        print(f"Error during login verification: {e}")
        assert False, "Login verification failed"


@then(u'verify successful message')
def succes_message(context):
    element = context.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/header/div[1]/span')
    print(element.text)


@then(u'close browser')
def close_browser(context):
    context.driver.quit()

def tri(n):
    if n % 2 == 0:
        print("even number")
    else:
        print("none")

