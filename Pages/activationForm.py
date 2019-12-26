from selenium.webdriver.support.select import Select


class ActivationForm():
    def __init__(self, driver):
        self.driver = driver
        self.first_name = "//input[@name='firstName']"
        self.last_name = "//input[@name='lastName']"
        self.email = "//input[@name='email']"
        self.country_code = "//select[@name='countryCode']"
        self.contact_number = "//input[@name='phone']"
        self.password = "//input[@name='password']"
        self.confirm_password = "//input[@name='confirmPassword']"

    def enter_username(self, firstname, lastname):
        self.driver.find_element_by_xpath(self.first_name).send_keys(firstname)
        self.driver.find_element_by_xpath(self.last_name).send_keys(lastname)
        print("Name Filled")

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email).send_keys(email)
        print("Email Filled")

    def select_country_code(self, country_code):
        select = Select(self.driver.find_element_by_xpath(self.country_code))
        select.select_by_value(country_code)
        print("Country code selected")

    def enter_contact_number(self, contact_number):
        self.driver.find_element_by_xpath(self.contact_number).send_keys(contact_number)
        print("Contact number filled")

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password).send_keys(password)
        print("Password filled")

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element_by_xpath(self.confirm_password).send_keys(confirm_password)
        print("Confirm password filled")