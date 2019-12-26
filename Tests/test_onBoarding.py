from selenium import webdriver
from Pages.activationForm import ActivationForm
import time
import pytest


class TestSignup():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="../ExternalFiles/chromedriver.exe")
        driver.maximize_window()
        time.sleep(1)

    def test_signup(self, test_setup):
        signup = ActivationForm(driver)

        driver.get("https://uat.vertofx.com")
        print("Webpage opened successfully")
        time.sleep(2)

        signup_link = driver.find_element_by_xpath("//a[@routerlink='/auth/register']")
        signup_link.click()
        print("Signup link clicked")
        time.sleep(2)

        # Fill User Activation Form
        signup.enter_username("Anil", "Kumar")
        signup.enter_email("anil2212@mailinator.com")
        signup.select_country_code("+91")
        signup.enter_contact_number("2212130220")
        signup.enter_password("Password@123")
        signup.enter_confirm_password("Password@123")
