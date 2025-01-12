"""
Test case ID:TC_login_01

Test objective:
  Successful employee login to OrangeHRM Portal
Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
 1.In the login panel,enter the user name(Test data: “Admin”)
2.Enter the password for ESS User account in the password field (Test data:”admin123”)
3.Click”login”button

 Expected result:
The user is logged successfully
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located(self.username_locator))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(self.password_locator))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button_locator))
        login_button.click()
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.dashboard_header_locator = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_visible(self):
        dashboard_header = self.wait.until(EC.presence_of_element_located(self.dashboard_header_locator))
        return dashboard_header.is_displayed()

from selenium import webdriver

# Test case ID and objective
test_case_id = "TC_login_01"
test_objective = "Successful employee login to OrangeHRM Portal"

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Launch the OrangeHRM site
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Initialize the page objects
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Perform login
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()

    # Verify login
    if dashboard_page.is_dashboard_visible():
        print(f"{test_case_id}: {test_objective} - Passed")
    else:
        print(f"{test_case_id}: {test_objective} - Failed: Dashboard not visible")

except Exception as e:
    # Capture and display any errors
    print(f"{test_case_id}: {test_objective} - Failed. Error: {str(e)}")
finally:
    # Close the browser
    driver.quit()

"""
Test case ID:TC_login_02

Test objective:
Invalid employee login to orangeHRM portal

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
 1.In the login panel,enter the user name(Test data: “Admin”)
2.Enter the password for ESS User account in the password field (Test data:”admin123”)
3.Click”login”button

 Expected result:
A valid error message displayed for invalid credentials is displayed.

TestCases dealing with the PIM:
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")
        self.error_message_locator = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located(self.username_locator))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(self.password_locator))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button_locator))
        login_button.click()

    def get_error_message(self):
        """Retrieve the error message displayed for invalid credentials."""
        error_message_element = self.wait.until(EC.visibility_of_element_located(self.error_message_locator))
        return error_message_element.text


# Test Case Implementation
from selenium import webdriver

# Test case ID and objective
test_case_id = "TC_login_02"
test_objective = "Invalid employee login to OrangeHRM portal"

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Launch the OrangeHRM site
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Step 2: Initialize the page object
    login_page = LoginPage(driver)

    # Step 3: Enter invalid login credentials
    login_page.enter_username("Admin")
    login_page.enter_password("wrongpassword")
    login_page.click_login_button()

    # Step 4: Verify the error message
    error_message = login_page.get_error_message()
    expected_error_message = "Invalid credentials"

    assert expected_error_message in error_message, \
        f"Expected error message '{expected_error_message}', but got '{error_message}'"

    # Test passed
    print(f"{test_case_id}: {test_objective} - Passed")

except AssertionError as ae:
    # Handle assertion errors separately
    print(f"{test_case_id}: {test_objective} - Failed. Assertion Error: {str(ae)}")
except Exception as e:
    # Handle any other exceptions
    print(f"{test_case_id}: {test_objective} - Failed. Error: {str(e)}")
finally:
    # Close the browser
    driver.quit()


"""
Test case ID:TC_PIM_01

Test objective:
Add a new employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser
Steps:
1.Go to PIM Module from the left pane in the web page.
2.Click on Add and add new employee details in the page
3.Fill in all the personal details of the employee and click save

Expected Result:
The user should be able to add new employee in the PIM and should see a message successful employee addition.

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        """Perform login action."""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
            print("Login successful.")
        except TimeoutException:
            raise Exception("Login elements not found within the timeout period.")


# PIM Page POM
class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.pim_menu_locator = (By.XPATH, "//span[text()='PIM']")
        self.add_button_locator = (By.XPATH, "//button[text()=' Add ']")
        self.first_name_locator = (By.NAME, "firstName")
        self.last_name_locator = (By.NAME, "lastName")
        self.save_button_locator = (By.XPATH, "//button[@type='submit']")
        self.success_message_locator = (By.XPATH, "//div[contains(@class, 'oxd-alert--success')]")

    def navigate_to_pim(self):
        """Navigate to the PIM module."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.pim_menu_locator)).click()
            print("Navigated to the PIM module.")
        except TimeoutException:
            raise Exception("Failed to navigate to PIM module.")

    def add_employee(self, first_name, last_name):
        """Add a new employee in the PIM module."""
        try:
            # Click on Add button
            self.wait.until(EC.element_to_be_clickable(self.add_button_locator)).click()

            # Fill in employee details
            self.wait.until(EC.presence_of_element_located(self.first_name_locator)).send_keys(first_name)
            self.wait.until(EC.presence_of_element_located(self.last_name_locator)).send_keys(last_name)

            # Save the new employee
            self.wait.until(EC.element_to_be_clickable(self.save_button_locator)).click()
            print(f"Employee '{first_name} {last_name}' added successfully.")
        except TimeoutException:
            raise Exception("Error adding employee.")

    def verify_success_message(self, expected_message):
        """Verify the success message after an action."""
        try:
            success_message = self.wait.until(EC.visibility_of_element_located(self.success_message_locator)).text
            print(f"Success message displayed: {success_message}")
            return expected_message in success_message
        except TimeoutException:
            print("Success message not found.")
            return False


# Test Case Implementation (Add Employee only)
def test_add_employee():
    """Test case for adding an employee in the PIM module."""
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    new_first_name = "Michael"
    new_last_name = "Jordan"

    expected_add_message = "Successfully Saved"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(base_url)
        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)

        # Login
        login_page.login(username, password)

        # Navigate to PIM Module
        pim_page.navigate_to_pim()

        # Add a new employee
        pim_page.add_employee(new_first_name, new_last_name)

        # Verify success message after adding employee
        if pim_page.verify_success_message(expected_add_message):
            print("Add Employee: Test Case Passed.")
        else:
            print("Add Employee: Test Case Failed. Success message not displayed.")
    except Exception as e:
        print(f"Test Case Failed: {str(e)}")
    finally:
        driver.quit()


# Run the Test
test_add_employee()

"""
Test case ID:TC_PIM_02

Test objective:
Edit an existing employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser
Steps:
1.Go to PIM Module from the left pane in the web page.
2.From the existing list of Employees in the PIM Module.
edit the employee information of the employee and save it.

Expected Result:
The user should be able to edit an existing employee information in the PIM and should see a message successful employee details addition.


"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        """Perform login action."""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
            print("Login successful.")
        except TimeoutException:
            raise Exception("Login elements not found within the timeout period.")


# PIM Page POM
class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.pim_menu_locator = (By.XPATH, "//span[text()='PIM']")
        self.employee_list_locator = (By.XPATH, "//a[text()='Employee List']")
        self.edit_button_locator = (By.XPATH, "//button[contains(@class, 'oxd-button--secondary')]")  # Edit button in the employee list
        self.first_name_locator = (By.NAME, "firstName")
        self.last_name_locator = (By.NAME, "lastName")
        self.save_button_locator = (By.XPATH, "//button[@type='submit']")
        self.success_message_locator = (By.XPATH, "//div[contains(@class, 'oxd-alert--success')]")

    def navigate_to_pim(self):
        """Navigate to the PIM module."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.pim_menu_locator)).click()
            print("Navigated to the PIM module.")
        except TimeoutException:
            raise Exception("Failed to navigate to PIM module.")

    def navigate_to_employee_list(self):
        """Navigate to the Employee List page."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.employee_list_locator)).click()
            print("Navigated to Employee List.")
        except TimeoutException:
            raise Exception("Failed to navigate to Employee List.")

    def edit_employee(self, employee_name, new_first_name, new_last_name):
        """Edit an existing employee's details."""
        try:
            # Search for employee by name
            employee_row_locator = (By.XPATH, f"//div[contains(text(), '{employee_name}')]//ancestor::tr")
            employee_row = self.wait.until(EC.presence_of_element_located(employee_row_locator))
            employee_row.click()

            # Click the Edit button
            self.wait.until(EC.element_to_be_clickable(self.edit_button_locator)).click()

            # Modify employee details
            self.wait.until(EC.presence_of_element_located(self.first_name_locator)).clear()
            self.wait.until(EC.presence_of_element_located(self.first_name_locator)).send_keys(new_first_name)
            self.wait.until(EC.presence_of_element_located(self.last_name_locator)).clear()
            self.wait.until(EC.presence_of_element_located(self.last_name_locator)).send_keys(new_last_name)

            # Save changes
            self.wait.until(EC.element_to_be_clickable(self.save_button_locator)).click()
            print(f"Employee details updated to: {new_first_name} {new_last_name}.")
        except TimeoutException:
            raise Exception("Error editing employee.")

    def verify_success_message(self, expected_message):
        """Verify the success message after an action."""
        try:
            success_message = self.wait.until(EC.visibility_of_element_located(self.success_message_locator)).text
            print(f"Success message displayed: {success_message}")
            return expected_message in success_message
        except TimeoutException:
            print("Success message not found.")
            return False


# Test Case Implementation (Edit Employee only)
def test_edit_employee():
    """Test case for editing an existing employee's details."""
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    employee_name = "Michael Jordan"  # Existing employee to edit
    new_first_name = "Mike"
    new_last_name = "Jordan"

    expected_edit_message = "Successfully Saved"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(base_url)
        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)

        # Login
        login_page.login(username, password)

        # Navigate to PIM Module
        pim_page.navigate_to_pim()

        # Navigate to Employee List
        pim_page.navigate_to_employee_list()

        # Edit an existing employee
        pim_page.edit_employee(employee_name, new_first_name, new_last_name)

        # Verify success message after editing employee
        if pim_page.verify_success_message(expected_edit_message):
            print("Edit Employee: Test Case Passed.")
        else:
            print("Edit Employee: Test Case Failed. Success message not displayed.")
    except Exception as e:
        print(f"Test Case Failed: {str(e)}")
    finally:
        driver.quit()


# Run the Test
test_edit_employee()

"""

Test case ID:TC_PIM_03

Test objective:
Delete an existing employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
1.Go to PIM Module from the left pane in the web page.
2.From the existing list of Employees in the PIM Module.delete an existing employee.

Expected Result:
The user should be able to delete an existing employee information in the PIM and should see a message successful deletion.


"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Login Page POM
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        """Perform login action."""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button_locator)).click()
            print("Login successful.")
        except TimeoutException:
            raise Exception("Login elements not found within the timeout period.")


# PIM Page POM
class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Locators
        self.pim_menu_locator = (By.XPATH, "//span[text()='PIM']")
        self.employee_list_locator = (By.XPATH, "//a[text()='Employee List']")
        self.edit_button_locator = (By.XPATH, "//button[contains(@class, 'oxd-button--secondary')]")  # Edit button in the employee list
        self.delete_button_locator = (By.XPATH, "//button[contains(@class, 'oxd-button--danger')]")  # Delete button in the employee list
        self.first_name_locator = (By.NAME, "firstName")
        self.last_name_locator = (By.NAME, "lastName")
        self.save_button_locator = (By.XPATH, "//button[@type='submit']")
        self.success_message_locator = (By.XPATH, "//div[contains(@class, 'oxd-alert--success')]")
        self.confirm_delete_button_locator = (By.XPATH, "//button[contains(text(), 'Yes, Delete')]")  # Confirm deletion button

    def navigate_to_pim(self):
        """Navigate to the PIM module."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.pim_menu_locator)).click()
            print("Navigated to the PIM module.")
        except TimeoutException:
            raise Exception("Failed to navigate to PIM module.")

    def navigate_to_employee_list(self):
        """Navigate to the Employee List page."""
        try:
            self.wait.until(EC.element_to_be_clickable(self.employee_list_locator)).click()
            print("Navigated to Employee List.")
        except TimeoutException:
            raise Exception("Failed to navigate to Employee List.")

    def delete_employee(self, employee_name):
        """Delete an existing employee's details."""
        try:
            # Search for employee by name in the employee list
            employee_row_locator = (By.XPATH, f"//div[contains(text(), '{employee_name}')]//ancestor::tr")
            self.wait.until(EC.presence_of_element_located(employee_row_locator))  # Ensure the employee row is present
            employee_row = self.driver.find_element(*employee_row_locator)
            employee_row.click()

            # Click the Delete button
            self.wait.until(EC.element_to_be_clickable(self.delete_button_locator)).click()

            # Confirm deletion
            self.wait.until(EC.element_to_be_clickable(self.confirm_delete_button_locator)).click()
            print(f"Employee {employee_name} deleted.")
        except TimeoutException:
            raise Exception("Error deleting employee. Could not find or delete the employee.")

    def verify_success_message(self, expected_message):
        """Verify the success message after an action."""
        try:
            success_message = self.wait.until(EC.visibility_of_element_located(self.success_message_locator)).text
            print(f"Success message displayed: {success_message}")
            return expected_message in success_message
        except TimeoutException:
            print("Success message not found.")
            return False


# Test Case Implementation (Delete Employee)
def test_delete_employee():
    """Test case for deleting an existing employee's details."""
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    employee_name = "Michael Jordan"  # Employee to delete

    expected_delete_message = "Successfully Deleted"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(base_url)
        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)

        # Login
        login_page.login(username, password)

        # Navigate to PIM Module
        pim_page.navigate_to_pim()

        # Navigate to Employee List
        pim_page.navigate_to_employee_list()

        # Delete an existing employee
        pim_page.delete_employee(employee_name)

        # Verify success message after deleting employee
        if pim_page.verify_success_message(expected_delete_message):
            print("Delete Employee: Test Case Passed.")
        else:
            print("Delete Employee: Test Case Failed. Success message not displayed.")
    except Exception as e:
        print(f"Test Case Failed: {str(e)}")
    finally:
        driver.quit()


# Run the Test
test_delete_employee()


